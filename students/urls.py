from django.urls import path
from .views import RegisterForm,LoginForm,UserProfileView,LogoutView,StudentListView,StudentCreateView,StudentUpdateView,StudentDeleteView,StudentDetailsView


urlpatterns = [
    # user urls
    path('register/', RegisterForm.as_view(), name='register'),
    path('login/', LoginForm.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),

    # students urls
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/update/<int:student_id>/', StudentUpdateView.as_view(), name='student_update'),
    path('students/details/<int:student_id>/', StudentDetailsView.as_view(), name='student_details'),
    path('students/delete/<int:student_id>/', StudentDeleteView.as_view(), name='student_delete'),
]
