# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after successful signup
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    return render(request, 'login.html')

# View for the home page
def home(request):
    return render(request, 'home.html')

# View for the about page
def about(request):
    return render(request, 'about_us.html')
