# Django CRM Project

This Django project provides a simple web application for managing records, user authentication, and password reset functionalities. Users can register, log in, create, edit, and delete records. Additionally, the project includes email-based activation and password reset features.

**Note: Before getting started, ensure to configure the database and email settings in the `settings.py` file.**

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [License](#license)

## Project Overview

This Django project is structured to manage records associated with user accounts. Users can perform various actions such as creating, editing, and deleting records. The project also includes user authentication features, ensuring secure access to the application. Furthermore, users receive activation emails upon registration and can reset their passwords through email-based links.

## Features

- User Registration and Authentication
- Email Activation for User Accounts
- Password Reset via Email
- Create, Edit, and Delete Records
- Search and Filter Records

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/henalon0/django-crm-project
   ```

2. **Navigate to the project directory:**

   ```bash
   cd django-crm-project
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```

   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser account (optional):**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at [http://localhost:8000](http://localhost:8000).

## Usage

1. **Access the application:**

   Open a web browser and go to [http://localhost:8000](http://localhost:8000).

2. **Register a new account:**

   Navigate to the registration page, fill in the required details, and submit the form. Check your email for an activation link.

3. **Activate your account:**

   Click on the activation link received in your email to activate your account.

4. **Log in:**

   Use your registered credentials to log in to the application.

5. **Manage Records:**

   - **Create Record:** Add new records through the "Create" page.
   - **Edit Record:** Modify existing records on the "Edit" page.
   - **Delete Record:** Remove records from the "Home" page.

6. **Search and Filter Records:**

   Utilize the search bar on the "Home" page to find specific records based on various criteria.

7. **Logout:**

   Log out from your account using the "Logout" link.

## Dependencies

The project utilizes the following dependencies:

- Django
- Python
- Other dependencies are listed in the `requirements.txt` file.

## License

This project is licensed under the [MIT License](LICENSE).
