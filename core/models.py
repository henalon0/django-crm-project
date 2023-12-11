from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at.strftime(r'%d-%m-%Y %H:%M:%S') + ' - ' + self.first_name + ' ' + self.last_name + ' - ' \
            + self.email + ' - ' + self.phone + ' - ' + self.city + ' - ' + self.state
