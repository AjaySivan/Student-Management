from django.urls import path
from . import views

urlpatterns = [
    path('',views.display_studentdata),
    path('register/',views.student_registration),
]