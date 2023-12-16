from django.shortcuts import render,HttpResponse,redirect
from contents.models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

 

# Create your views here.
def home(request):
    # return HttpResponse('this is working')
    return render(request, 'index.html')

def contacts(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        email= request.POST.get('email')
        comment=request.POST.get('comments')
        contact_data=contact(name=name, email=email, content=comment, date=datetime.today())
        contact_data.save()
        messages.get_messages(request)
        messages.success(request, "Message has been sent.")
    return render(request,'contact.html')
    

def services(request):
    return render(request,'services.html')

def portfolio(request):
    return render(request,'portfolio.html')

def logout_p(request):
    logout(request)
    return render(request,'login.html')

def landing(request):

    if request.method == 'POST':
        # Process POST request and save form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        current_role = request.POST.get("role")
        recommend = request.POST.get("customRadioInline1")
        useful = request.POST.get("val")
        username=request.user
        message = request.POST.get("comment")
        print(name,email,message)
        form_data = Form(name=name, email=email, age=age, current_role=current_role, recommend=recommend, useful=useful,username=username, message=message)
        form_data.save()
    return render(request, 'landing.html')
         # Redirect after form submission
    
    
    # return render(request,'landing.html')


def viewform(request):
    if request.user.is_authenticated:

        username=request.user
        form_datas = Form.objects.filter(username=username)
        return render(request, 'viewform.html', {'form_datas': form_datas})
    else:
        return redirect('login')
    # form_datas=Form.objects.all()
    
def pratice(request):
    all_data=form_d.objects.all()
    return render(request, 'pratice.html', {'all_data': all_data})
 
def login_p(request):
    # if request.method =='POST':
    #     user_name = request.POST["Username"]
    #     password = request.POST["Password"]
    #     print(user_name, password)
    #     user = authenticate(request, username=user_name, password=password)
    #     if user is not None:
    #         login(request, user)
    #         # Redirect to a success page.
    #         return redirect('/landing.html')
    #     else:
    #         # Return an 'invalid login' error message.
    #         return redirect("/login")

    # return render(request,'login.html')

    if request.user.is_authenticated: 
        return render(request,'landing.html')
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/landing')  # Replace 'success_url' with your desired success URL
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'login.html')

def pratice(request):
    all_data=form_d.objects.all()
    return render(request, 'pratice.html', {'all_data': all_data})
    
def add_d(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        data=form_d(name=name, email=email, address=address, phone=phone)
        data.save()
        return redirect('pratice')
    
# def edit(request):
#     all_data=form_d.objects.all()
#     return redirect(request, 'pratice.html', {'all_data': all_data})
    
def update(request,id):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        data=form_d(id=id,name=name, email=email, address=address, phone=phone)
        data.save()
        return redirect('pratice')
    return redirect(request,'pratice.html')

def delete(request,id):
    asd=form_d.objects.filter(id=id).delete()
    return redirect('pratice')



