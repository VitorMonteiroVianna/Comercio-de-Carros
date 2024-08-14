from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('cars_list')
        
    else:
        user_creation_form = UserCreationForm()
    
    return render(request, 'register_user.html', {"user_creation_form": user_creation_form})