from django.shortcuts import render,redirect

from .form import MemberForm,SignupForm

# Create your views here.
def opening(request):
    context={
        'opening':'opening'
    }
    return render(request,'opening.html',context)
def login(request):
    form= MemberForm()
    return render(request,'login.html',{'form':form})

def signUp(request):
    if request.method == "POST":
        form= SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=SignupForm()
    return render(request,'signup.html',{'form':form})