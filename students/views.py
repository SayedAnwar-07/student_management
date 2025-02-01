from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import UserRegisterForm, StudentForm
from .models import Student


# register class
class RegisterForm(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'students/auth/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        return render(request, 'students/auth/register.html', {'form': form})


# login class
class LoginForm(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, 'students/auth/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        return render(request, 'students/auth/login.html', {'form': form})


# logout class
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


# profile class 
class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        students = Student.objects.filter(user=user)
        return render(request, 'students/auth/profile.html', {'user': user, 'students': students})

# Student list view class
class StudentListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        students = Student.objects.filter(user=request.user)
        return render(request, 'students/student_info/student_list.html', {'students': students})


# Student create view class
class StudentCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = StudentForm()
        return render(request, 'students/student_info/student_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('student_list')
        return render(request, 'students/student_info/student_form.html', {'form': form})


# Student update view class
class StudentUpdateView(LoginRequiredMixin, View):
    def get(self, request, student_id, *args, **kwargs):
        student = get_object_or_404(Student, id=student_id, user=request.user)
        form = StudentForm(instance=student)
        return render(request, 'students/student_info/student_form.html', {'form': form})

    def post(self, request, student_id, *args, **kwargs):
        student = get_object_or_404(Student, id=student_id, user=request.user)
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        return render(request, 'students/student_info/student_form.html', {'form': form})


# Student details page view class
class StudentDetailsView(LoginRequiredMixin, View):
    def get(self, request, student_id, *args, **kwargs):
        student = get_object_or_404(Student, id=student_id, user=request.user)
        return render(request, 'students/student_info/student_info.html', {'student': student})


# Student delete view class
class StudentDeleteView(LoginRequiredMixin, View):
    def get(self, request, student_id, *args, **kwargs):
        student = get_object_or_404(Student, id=student_id, user=request.user)
        return render(request, 'students/student_info/student_confirm_delete.html', {'student': student})

    def post(self, request, student_id, *args, **kwargs):
        student = get_object_or_404(Student, id=student_id, user=request.user)
        student.delete()
        return redirect('student_list')
