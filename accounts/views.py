from accounts.models import Payments
from django.contrib.auth import authenticate, login as lin, logout as lout
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from pypaystack import Transaction


from .forms import CustomUserCreationForm, PaymentsForm, UserProfileForm

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
    queryset = Payments.objects.all()

    content = {
        'queryset': queryset,
    }
    
    return render(request, "accounts/dashboard.html", content)

def payment(request):
    if request.method == 'POST':
        pay_form = PaymentsForm(request.POST, request.FILES, instance=request.user.payments)

        if pay_form.is_valid():

            pay_form.save()
            return redirect('youth:sermons')

    else:
        pay_form = PaymentsForm(instance=request.user.payments)
        date = Payments.scheduled_at.date()
        content = {
            'pay_form': pay_form,
            'date': date,
        }
        return render(request, "accounts/payment.html", content)


# def payment(request):
#     if request.method == "POST":
#         print(request.POST)
#         if request.POST.get('fullname') and request.POST.get('email') and request.POST.get('mobile_number') and request.POST.get("amount"):
#             people = Payments()
#             people.fullname = request.POST.get('fullname')
#             people.email = request.POST.get('email')
#             people.mobile_number = request.POST.get('mobile_number')
#             people.types = request.POST.get('type')
#             people.amount = request.POST.get("amount")
#             people.save()
#             return render(request, "youth/sermons.html")
#     else:
#         return render(request, "accounts/payment.html")    
    

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

