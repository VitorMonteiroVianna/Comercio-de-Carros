from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate


def register_view(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('authenticate_user')
        
    else:
        user_creation_form = UserCreationForm()
    
    return render(request, 'register_user.html', {"user_creation_form": user_creation_form})


def authenticate_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user_in_db = authenticate(request, username=username, password=password)
        if user_in_db is not None:
            login(request, user_in_db)
            return redirect('cars_list')
        else:
            user_authentication_form = AuthenticationForm()
        
    else:
        user_authentication_form = AuthenticationForm()
    
    return render(request, 'authenticate_user.html', {"user_authentication_form": user_authentication_form})