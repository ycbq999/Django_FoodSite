from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # save the user
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'welcome {username}! your account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request): 
    logout(request)     
    return render(request, 'users/logout.html')

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')
