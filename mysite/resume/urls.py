from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.resume_view, name='resume'),  # Define the route for the resume view
]
