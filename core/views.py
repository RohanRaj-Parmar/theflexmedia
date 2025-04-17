from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerRequestForm

def home(request):
    return render(request, 'core/home.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request has been submitted successfully! We'll contact you soon.")
            return redirect('contact')
    else:
        form = CustomerRequestForm()
    
    return render(request, 'core/contact.html', {'form': form})