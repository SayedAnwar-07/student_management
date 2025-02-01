# Student Management System

A Django-based Student Management System that allows users to register, log in, and manage student information (create, update, list, delete, view details). Admin users can manage student data and view student profiles.

## Features

- User Authentication (Register, Login, Logout)
- Profile Management
- CRUD Operations for Students
  - List students
  - Create a new student
  - Update student information
  - Delete student records
  - View student details

## Technologies Used

- Django 5.1.4
- Python 3.x
- SQLite (default DB)
- Bootstrap (for frontend UI)

## Directory Structure

. ├── students/ │ ├── auth/ # Authentication views (Login, Register, Logout) │ │ ├── register.html │ │ ├── login.html │ │ └── profile.html │ ├── student_info/ # Student-related views and templates │ │ ├── student_list.html │ │ ├── student_form.html │ │ ├── student_info.html │ │ └── student_confirm_delete.html │ ├── forms.py # UserRegistration and Student forms │ ├── models.py # Student model definition │ └── urls.py # Routing for student views ├── manage.py ├── requirements.txt # Project dependencies └── README.md


## Setup

1. Clone the repository:
git clone https://github.com/yourusername/student-management.git cd student-management

2. Install dependencies:

3. Apply migrations:

4. Create a superuser (for admin access):

5. Run the development server:

6. Access the app at `http://127.0.0.1:8000/`.

## Views

- **RegisterForm**: Allows users to register.
- **LoginForm**: Allows users to log in.
- **LogoutView**: Logs out the user.
- **UserProfileView**: Displays the logged-in user's profile and associated students.
- **StudentListView**: Lists all students of the logged-in user.
- **StudentCreateView**: Creates a new student.
- **StudentUpdateView**: Updates existing student information.
- **StudentDetailsView**: Displays details of a student.
- **StudentDeleteView**: Confirms and deletes a student.

## Templates

- **students/auth/register.html**: Registration form for users.
- **students/auth/login.html**: Login form for users.
- **students/auth/profile.html**: Displays user profile and students.
- **students/student_info/student_list.html**: Displays list of students.
- **students/student_info/student_form.html**: Form to create or update a student.
- **students/student_info/student_info.html**: Displays student details.
- **students/student_info/student_confirm_delete.html**: Confirmation page for student deletion.

## Models

- **Student**: Stores student information (name, email, phone number, course, image, created_at, updated_at).

## URLs

- `students/`: Student management views for listing, creating, updating, and deleting students.
- `students/register/`: User registration page.
- `students/login/`: User login page.
- `students/logout/`: User logout action.
- `students/profile/`: User profile page.

## License

This project is licensed under the MIT License.
