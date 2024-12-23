# urls.py
from django.contrib import admin
from django.urls import path
from lgbtfrontend.views import home, about, signup_view  # Import signup_view directly
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('about/', about, name='about'),  # About page
    path('signup/', signup_view, name='signup'),  # Signup page
    path('login/', views.login_view, name='login'),
]


