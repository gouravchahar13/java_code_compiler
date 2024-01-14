from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .mail import *
from .compiler import compile_code
import asyncio  


# Create your views here.

#basic show
def home(request):
    context={'title':"Java Compiler"}
    return render(request,'index.html',context)

#user_accounts
#signup
def Signup_view(request):
    if request.method=='POST':
        form=Signup_Form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            # reg_mail()
            messages.info(request,'account created successfully')
            return redirect('login_pg')
        else:
            messages.info(request,'the details are not entered correctly')
            return redirect('login_pg')
    context={'title':'Signup','form':Signup_Form()}
    return render(request,'register_login/signup.html',context)

#login
def login_page(request):
    if request.method=='POST':
        form=Login_form(request.POST)
        if form.is_valid():
            data=request.POST
            username=data.get('username')
            password=data.get('password')
            if not User.objects.filter(username=username).exists():
                messages.info(request,'Invalid username')
                return redirect('login_pg')
            user=authenticate(username=username,password=password)  
            if user is None:
                messages.info(request,'Invalid username/Password')    
                return redirect('login_pg')      
            login(request,user)
            messages.info(request,'You have successfully logged into the site')            
            return redirect('main')
        else:
            messages.info(request,'please fill the captcha correctly')
            return redirect('/login/')
    context={'title':'Login','form':Login_form()}
    return render(request,'register_login/login.html',context)

@login_required(login_url='login_pg')
def log_out(request,username):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')

@login_required(login_url='login_pg')
def delete_user(request,username):
    u = User.objects.get(username = username)
    u.delete()
    # delete_mail()
    messages.info(request, "Acoount deleted successfully")
    return redirect('home')

#user accounts ends

async def main(code): 
    print('compiling...')  
    response=await compile_code(code)  
    return (response['output']) 

#main
@login_required(login_url='/login/')
def code_compiler(request):
    context={'title':'Java_compiler:Code'}
    if request.method=='POST':
        data=request.POST
        code=data['code']
        output= asyncio.run(main(code)) 
        print(output)
        context={'title':'Java_compiler:Code','code':code,'output':output}
        return render(request,'main.html',context)
    return render(request,'main.html',context)