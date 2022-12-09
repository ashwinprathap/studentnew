from django.shortcuts import redirect,render
from .models import Students
# from .forms import StudentForm
from django.views import View
from account.models import Staff,Contact

class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Enquery(View):
    def get(self,request):
        customer=Contact.objects.all()
        return render(request, 'enquery.html',{'form':customer})