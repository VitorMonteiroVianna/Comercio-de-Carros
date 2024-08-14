from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    user_creation_form = UserCreationForm()
    return render(request, 'register_user.html', {"user_creation_form": user_creation_form})