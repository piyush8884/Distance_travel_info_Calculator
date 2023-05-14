from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime

import google_maps.all
from home.models import Contact
from django.contrib import messages
from google_maps.distance_calcy import *
from google_maps.all import *
# def index(request):
#    # return HttpResponse("This is MY page")
#     return render(request,"index.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        subject = request.POST.get("subject")
        contacts=Contact(name=name,email=email,subject=subject,desc=desc,date=datetime.today())
        contacts.save()
        messages.success(request,'Your message has been sent')
        return redirect('thankyou')
    return render(request,'contact.html')

def index(request):
    data=None
    if request.method == 'POST':
        Place_1 = request.POST.get('OriginCity')
        Place_2 = request.POST.get('DestinationCity')
        # do something with name and email
        data = google_maps.distance_calcy.place_search(Place_1,Place_2)
        output_str = "\n".join([f"{k}======{v}" for k, v in data.items()])
        data = output_str
    return render(request, 'index.html',{'data': data})


def thankyou(request):
    return render(request, 'thankyou.html')

# Create your views here.
