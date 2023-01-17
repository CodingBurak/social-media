from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm

# Create your views here.
def user_login(request):
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      user = authenticate(request=request,username=data["username"], password= data["password"])
      if user is not None:
        login(request, user=user)
        return HttpResponse("successful logged in")
      else:
        return HttpResponse("user not existing")
  else:
    form = LoginForm()
  return render(request, "users/login.html", {"form": form})


@login_required
def index(request):
  return render(request, "users/index.html")

def register(request):
  form = UserRegistrationForm()
  if request.method == "POST":
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      new_user = form.save(commit=False)
      new_user.set_password(form.cleaned_data["password"])
      new_user.save()
      return render(request, "users/register_done.html")
  return render(request, "users/register.html", {"form": form})