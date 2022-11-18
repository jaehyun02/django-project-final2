from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from users.models import Member
from .form import BoardWriteForm
from .models import Board

# Create your views here.
def main(request):
    boardList= Board.objects.all()
    if request.method == 'POST':
        username=request.POST.get('username')
        password= request.POST.get('password')
        user= Member.objects.get(username=username,password=password) 
            
        if user is not None:
            request.session['userid']=user.id
            return render(request,'main.html',{'boardList':boardList})
        else:
            return redirect('login')
    return render(request,'main.html',{'boardList':boardList})

def write(request):
    if request.method =='POST':
        form= BoardWriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/main')
    user_id=request.session['userid']
    user= get_object_or_404(Member,pk=user_id)
    form=BoardWriteForm(initial={'user':user})
    return render(request,'write.html',{'form':form,'user':user})

def detail(request,boardid):
    board= get_object_or_404(Board,pk=boardid)
    try:
        session=request.session['userid']
        context={
            'board':board,
            'session':session
        }
        return render(request,'detail.html',context)
    except KeyError:
        return redirect('/main')
    
def delete(request,boardid):
    board=Board.objects.get(pk=boardid)
    if request.method== 'POST':
        board.delete()
        return redirect('/main')
    return render(request,'delete.html',{'Board':board})