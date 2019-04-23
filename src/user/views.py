from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    template_name = 'user_register.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def profile(request):
    template_name = 'user_profile.html'
    return render(request, template_name)