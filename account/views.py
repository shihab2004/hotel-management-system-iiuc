from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout

# Create your views here.
def login_user(request):
    context = {}
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST.get("email"))
            if user.is_active:
                
                if not user.check_password(request.POST['password']): raise
                    
                login(request,user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                
                return redirect('/hotels/')
                
            else:context.update({"msg":"Sorry, This user is not allow."})
                
        except Exception as e:
            print(e)
            context.update({"msg":"Invalid credentials"})
    return render(request,"auth/login.html",context)


from django.contrib.auth.forms import UserCreationForm
def signup(request):
      form = UserCreationForm()
      
      context = {
          "form":form  
      }
      
      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              user.email = request.POST.get('email')
              user.save()
              return redirect("/auth/login/")
          else:
                context.update({"error":form.errors})
            
       
   
      return render(request,"auth/singup.html",context)

def logout_user(request):
    logout(request)
    return redirect('/auth/login')