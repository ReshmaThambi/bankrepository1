from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import District, ApplicationForm
from .models import Branch


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pass1 = request.POST['password']
        cpass = request.POST['password1']

        if pass1 == cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, password=pass1)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=uname, password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('welcome')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def welcome(request):
    return render(request, "welcome.html")


def form(request):

    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account = request.POST['account']
        materials = request.POST['materials']
        user1 = ApplicationForm(name=name, dob=dob, age=age, gender=gender, phone=phone,
                     email=email, address=address, district=district, branch=branch,
                     account=account, materials=materials)

        user1.save()
        messages.info(request, "application accepted")
    return render(request, "form.html")


def msg(request):
    return render(request, "msg.html")
