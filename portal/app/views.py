from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def helloworld(request):
    return render(request, 'hello.html')


def home(request):
    return render(request, 'home.html')


def signup(request):
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})