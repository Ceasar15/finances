from django.contrib.auth import authenticate, login as lin, logout as lout
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.views.generic.base import TemplateView

from .forms import CustomUserCreationForm, PaymentsForm, UserProfileForm
from accounts.models import Payments

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
        p_form=UserProfileForm(instance=request.user.profile)
        context={
            'p_form': p_form
            }
    return render(request, "accounts/profile.html", context)

@login_required
def dashboard(request):
    queryset = Payments.objects.filter(user=request.user)
    total = 0
    for pay2 in queryset:
        total += pay2.amount
    
    context = {
        'queryset': queryset,
        'total': total,
    }
    return render(request, "accounts/dashboard.html", context)

def donations(request):
    return render(request, "accounts/donations.html")

@login_required
def payment(request):
    if request.method == 'POST':
        print(request.POST)
        pay_form = PaymentsForm(request.POST, request.FILES)

        if pay_form.is_valid():
            obj = pay_form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, f'Your Payment has been Updated Successfully')
            return redirect('accounts:dashboard')
    else:
        return render(request, "accounts/payment.html")
    return render(request, "accounts/payment.html")
    

def logout(request):
    lout(request)
    return redirect('youth:index')

# def verify(request, reference):
#     transaction = Transaction(settings.PAYSTACK_SECRET_KEY)
#     response = transaction.verify(reference)
#     if response[3]['status'] == 'success':
#         return render(request, 'donations.html')
#     else:
#         return HttpResponse('failed')

