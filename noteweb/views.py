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
        return redirect("https://mynote-hrx9.onrender.com/viewNotes")

    return render(request,'index.html')

def viewnt(request):
    data = addNote.objects.all().values()
    context = {
       'data' : data,
    }
    return render(request,'viewnotes.html',context)

def viewSpecificNote(request,pk):
    noteinfo = addNote.objects.filter(id=pk).values()
    context={
        'noteinfo':noteinfo
    }
    return render(request,'viewspecificnote.html',context)

def edit(request,param):
    if request.method=='POST':
        note = addNote.objects.get(id=param)
        note.username = request.POST.get("username")
        note.email = request.POST.get("email")
        note.title = request.POST.get("title")
        note.desc = request.POST.get("desc")
        note.save()
        return redirect("https://mynote-hrx9.onrender.com/viewNotes")
    context = {
        'note': addNote.objects.get(id=param)
    }
    return render(request,'update.html',context)

def delete(request,param):
    d = addNote.objects.get(id=param)
    d.delete()
    return redirect('https://mynote-hrx9.onrender.com/viewNotes')

def deleteall(request):
    addNote.objects.all().delete()
    return redirect('https://mynote-hrx9.onrender.com/addNote')