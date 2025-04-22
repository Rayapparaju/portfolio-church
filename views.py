from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def home(request):
    return render (request, 'main/home.html')

def about(request):
    return render (request, 'main/about.html')

def service(request):
    return render (request, 'main/service.html')

def gallery(request):
    return render (request, 'main/gallery.html')

def contact(request):
    return render (request, 'main/contact.html')



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, "Thank you for contacting us!")
        return redirect('contact')

    return render(request, 'main/contact.html')
