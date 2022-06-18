from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        instance = Contact(name=name, email=email, phone=phone, desc=desc)
        instance.save()

    return render(request, 'contact.html')