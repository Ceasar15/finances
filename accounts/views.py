from django.contrib.auth import authenticate, login as lin, logout as lout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from pypaystack import Transaction


from .forms import CustomUserCreationForm, UserProfileForm

# register user
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)    
            new_user.save()

            messages.success(request, "Your account has been created successfully")
            return render(request, 'accounts/register.html')
        else:
            context = {
            'form': form,
        }
            return render(request, 'accounts/register.html', context)
 
    else:
        context = {
            'form': CustomUserCreationForm,
        }
        
        return render(request, 'accounts/register.html', context)
    

@login_required
def profile(request):
	if request.method == 'POST':
		
		p_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

		if p_form.is_valid():
			
			p_form.save()
			messages.success(request, f'Your Profile has been Updated Successfully')
			return redirect('accounts:dashboard')
	else:	
		
		p_form = UserProfileForm(instance=request.user.profile)
		context = {
			
			'p_form': p_form
		}
	return render(request, 'accounts/profile.html', context)


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")

def password_reset(request):
    return render(request, "accounts/password_reset_form.html")

def logout(request):
    lout(request)
    return redirect('youth:index')

def verify(request, reference):
    transaction = Transaction(settings.PAYSTACK_SECRET_KEY)
    response = transaction.verify(reference)
    if response[3]['status'] == 'success':
        return render(request, 'donations.html')
    else:
        return HttpResponse('failed')

