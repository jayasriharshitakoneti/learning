from travello.models import Destination
from django.shortcuts import render

# Create your views here.
def home(request):
    dest=Destination.objects.all()
    return render(request,"index.html",{'dest':dest})