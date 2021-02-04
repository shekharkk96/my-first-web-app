from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, Webpage
from . import forms
#from first_app.forms import forms
# Create your views here.

def index(request):
    my_dict={'insert_me':" Hi Shekhar You Have been inserted!"}
    return render(request,'first_app/index.html',context=my_dict)

def secondPage_data(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record':webpages_list}
    return render(request,'first_app/secondpg.html',context=date_dict)

def form_name_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VAlidation Success!")
            print("Name : "+ form.cleaned_data['name'])
            print("Email : "+ form.cleaned_data['email'])
            print("Text : "+ form.cleaned_data['text'])
    return render(request,'first_app/form.html',{'form':form})
