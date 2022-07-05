from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from online_judge.models import Problem

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('online_judge-home')
    else:
        form = UserRegisterForm()

    return render(request, 'Usersauthentication/register.html', {'form': form})
