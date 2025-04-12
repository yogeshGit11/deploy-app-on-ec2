from django.shortcuts import render
from .models import Student

# Create your views here.
def show(request):
    stud=Student.objects.all()
    return render(request,'index.html',{'stud':stud})