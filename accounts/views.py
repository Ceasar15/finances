from django.contrib.auth import authenticate, login as lin, logout as lout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm, UserProfileForm

# register user
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        #profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)    
            new_user.save()

            #profile_pic = profile_form.cleaned_data['profile_pic']
           # profile_form.save()

            messages.success(request, "Your account has been created successfully")
            return render(request, 'accounts/register.html')
        else:
            context = {
            'form': form,
         #   'profile_form': profile_form
        }
            return render(request, 'accounts/register.html', context)
 
    else:
        context = {
            'form': CustomUserCreationForm,
          #  'profile_form': UserProfileForm 
        }
        
        return render(request, 'accounts/register.html', context)
    

def dashboard(request):
    return render(request, "accounts/dashboard.html")

def password_reset(request):
    return render(request, "accounts/password_reset_form.html")

def logout(request):
    lout(request)
    return redirect('accounts:login')
