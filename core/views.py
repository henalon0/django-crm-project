from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, RecordForm, PasswordResetRequestForm, PasswordResetForm
from .models import Record

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token, password_reset_token

import json

@login_required(login_url='login')
def home(request):
    query = request.GET.get('query')
    if query:
        records = Record.objects.filter(created_by=request.user, first_name__icontains=query) | \
            Record.objects.filter(created_by=request.user, last_name__icontains=query) | \
            Record.objects.filter(created_by=request.user, email__icontains=query) | \
            Record.objects.filter(created_by=request.user, phone__icontains=query) | \
            Record.objects.filter(created_by=request.user, city__icontains=query) | \
            Record.objects.filter(created_by=request.user, state__icontains=query).order_by('-created_at')
    else:
        records = Record.objects.filter(created_by=request.user).order_by('-created_at')
    
    return render(request, 'index.html', {'records': records, 'query': query})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')  
        else:
            return render(request, 'login.html')
    

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                # Send activation email
                current_site = get_current_site(request)
                mail_subject = 'Activate your account'
                message = render_to_string('activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()

                messages.success(request, 'Account created successfully. Please check your email to activate your account.')
                return redirect('login')
            else:
                form_errors_json = json.loads(form.errors.as_json())
                first_key = list(form_errors_json.keys())[0]
                first_error = form_errors_json[first_key][0]['message']
                messages.error(request, first_error)

                return redirect('register')
        else:
            form = UserRegisterForm()
            return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated successfully. You can now log in.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link.')
        return redirect('login')
    

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        
        if form.is_valid():
            record = form.save(commit=False)
            record.created_by = request.user
            record.save()
            messages.success(request, 'Record created successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error creating record')
            return redirect('create')
    else:
        form = RecordForm()
        return render(request, 'create.html', {'form': form})


@login_required(login_url='login')
def edit(request, pk):
    record = Record.objects.get(id=pk)
    
    if record.created_by != request.user:
        messages.error(request, 'You are not authorized to edit this record')
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RecordForm(request.POST, instance=record)
            
            if form.is_valid():
                form.save()
                messages.warning(request, 'Record updated successfully')
                return redirect('home')
            else:
                messages.error(request, 'Error updating record')
                return redirect('edit', pk=pk)
        else:
            form = RecordForm(instance=record)
            return render(request, 'edit.html', {'form': form})
    

@login_required(login_url='login')
def delete(request, pk):
    record = Record.objects.get(id=pk)
    
    if record.created_by == request.user:
        record.delete()
        messages.error(request, 'Record deleted successfully')
    else:
        messages.error(request, 'You are not authorized to delete this record')
    
    return redirect('home')


def password_reset_request(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = PasswordResetRequestForm(request.POST)
            
            if form.is_valid():
                email = form.cleaned_data['email']
                associated_users = User.objects.filter(email=email)
                
                if associated_users.exists():
                    for user in associated_users:
                        # Send password reset email
                        current_site = get_current_site(request)
                        mail_subject = 'Reset your password'
                        message = render_to_string('password_reset_email.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': password_reset_token.make_token(user),
                        })
                        to_email = form.cleaned_data.get('email')
                        email = EmailMessage(mail_subject, message, to=[to_email])
                        email.send()
                        
                        messages.success(request, 'Password reset email sent. Please check your email to reset your password.')
                        return redirect('login')
                else:
                    messages.error(request, 'No account exists with that email address')
                    return redirect('password_reset_request')
            else:
                form_errors_json = json.loads(form.errors.as_json())
                first_key = list(form_errors_json.keys())[0]
                first_error = form_errors_json[first_key][0]['message']
                messages.error(request, first_error)
                
                return redirect('password_reset_request')
        else:
            form = PasswordResetRequestForm()
            return render(request, 'password_reset_request.html', {'form': form})
    

def password_reset(request, uidb64, token):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            
        if user is not None and password_reset_token.check_token(user, token):
            if request.method == 'POST':
                form = PasswordResetForm(request.POST)
                
                if form.is_valid():
                    password = form.cleaned_data['password1']
                    confirm_password = form.cleaned_data['password2']
                    
                    if password == confirm_password:
                        user.set_password(password)
                        user.save()
                        messages.success(request, 'Password reset successfully. You can now log in.')
                        return redirect('login')
                    else:
                        messages.error(request, 'Passwords do not match')
                        return redirect('password_reset', uidb64=uidb64, token=token)
                else:
                    form_errors_json = json.loads(form.errors.as_json())
                    first_key = list(form_errors_json.keys())[0]
                    first_error = form_errors_json[first_key][0]['message']
                    messages.error(request, first_error)
                    
                    return redirect('password_reset', uidb64=uidb64, token=token)
            else:
                form = PasswordResetForm()
                return render(request, 'password_reset.html', {'form': form})
        else:
            messages.error(request, 'Invalid password reset link.')
            return redirect('login')
    
        