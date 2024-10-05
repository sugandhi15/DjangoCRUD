from django.shortcuts import render,redirect
from noteweb.models import addNote


# Create your views here.
def home(request):
    return render(request,'home.html')

def add(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        note = addNote(username=username,email=email,title=title,desc=desc)
        note.save()


    return render(request,'index.html')

def viewnt(request):
    data = addNote.objects.all().values()
    context = {
       'data' : data,
    }
    return render(request,'viewnotes.html',context)


def delete(request,param):
    d = addNote.objects.get(id=param)
    d.delete()
    return redirect('http://127.0.0.1:8000/viewNotes')