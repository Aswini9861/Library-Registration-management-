from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import registration,Book
from .form import LoginForm
from .form import RegForm,BookForm

# Create your views here.
def home(request):
    return render(request,"index.html")




def signup(request):
    if(request.method=='POST'):
        form=RegForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponse("Registration Sucessfull!!!")
        else:
            print(form.errors)
    else:
        form=RegForm()
    return render(request,'signup.html',{'form':form})







def login(request):
    if(request.method=='POST'):
        form1=LoginForm(request.POST)
        if(form1.is_valid()):
            email=form1.cleaned_data['email']
            pwd=form1.cleaned_data['pwd']
            dbuser=registration.objects.filter(email=email,pwd=pwd)
            if(not dbuser):
                return HttpResponse('LOGIN FAILED')
            else:
                return render(request,"book_form.html")
    else:
        form1=LoginForm()
    return render(request,'login.html',{'form':form1})


def book_form(request,id=0):
    if(request.method=="GET"):
        if(id==0):
            form=BookForm()
        else:                  
            book=Book.objects.get(pk=id)
            form=BookForm(instance=book)
        return render(request,"book_form.html",{"form":form})
    else:
        if(id==0):
            form=BookForm(request.POST)

        else:        #update
            book=Book.objects.get(pk=id)  #filtering based on primarykey
            form=BookForm(request.POST,instance=book)
        if(form.is_valid()):
            form.save()
        return redirect('/library/list')




def book_list(request):
    context={'book_list':Book.objects.all()} 
    return render(request,"book_list.html",context)

def book_delete(request,id):
    book=Book.objects.get(pk=id)
    book.delete()
    return redirect('/library/list')