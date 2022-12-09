from django.shortcuts import render,redirect
from .models import Course,Contact,Staff
from django.contrib import messages

def mainhome(request):
    return render(request,'mainhome.html')

def signin(request):
    return render(request,'signin.html')
def signup(request):
    if request.method == "post":
        name=request.post['name']
        email=request.post['email']
        password=request.post['password']
        phno=request.post['phno']
        password2=request.post['password2']
        if password == password2:
            if Staff.objects.filter(email = email).exists():
                messages.info( request,"Email already taken")
                return redirect('signin')
            else:
                customer = Staff.objects.create(email = email,name= name,password = password,phno = phno)
                customer.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
                messages.info(request,'password is not matched')
                return redirect('signup')
            
    return render(request,'signup.html')
def forgot(request):
    return render(request,'forgot.html')
def course(request):
    courses={
        'course':Course.objects.all()
    }
    return render(request,'course.html')
    
def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')


def signin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            check_user=Staff.objects.get(email=email,password=password)
            request.session['email']=check_user.email
            request.session['name']=check_user.name
            request.session['phno']=check_user.phno
            return redirect('mainhome')
        except Staff.DoesNotExist:
            messages.error(request,'invalid username and password')
            return redirect('signin')
    return render(request,'signin.html')