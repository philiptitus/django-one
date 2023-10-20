from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from .models import Tlist
from .forms import New_User,UserProfileInfoform,Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.


def index(request):
    return render(request, 'todo/index.html')




@login_required
def records(request):
    title_dict = Tlist.objects.order_by('completion_date')
    real_dict = {'tasks':title_dict}

    return render(request,'todo/tasks.html',real_dict)



@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")


@login_required
def u_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def to_do(request):
    form = Task()

    if request.method == 'POST':
        form = Task(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("YOUR NEW TASK WAS SAVED SUCCESFULLY...")

        else:
            print("Invalid form was given")
            return HttpResponse("you did not fill in the form in a valid way")
        
    
    return render(request,'todo/todo_list.html',{'todo_list':form})
        


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = New_User(data=request.POST)
        profile_form = UserProfileInfoform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
           user = user_form.save()


           user.set_password(user.password)
           user.save()

          

           profile = profile_form.save(commit=False)
           

           profile.user = user

           registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        user_form = New_User()
        profile_form = UserProfileInfoform()

    
    return render(request, 'todo/register.html',
                  {'registered':registered,
                   'user_form':user_form,
                   'profile_form': profile_form,})


def u_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username,password=password)

        if user:

            if user.is_active:

                login(request,user)

                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("This account is no longer active sorry for any inconviniences caused..")
            
        else:
            print("SUSPICIOUS USER TRIED TO LOG IN")
            return HttpResponse("We do not recognise you")
            
    else:
      return render(request,'todo/login.html',{})
        

            

