from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        uname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['conpassword']

        if password == cpass:
            if User.objects.filter(username = uname):
                messages.info(request, 'username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name = first_name, username =uname, email = email, password = password)
                user.save()
                messages.success(request, 'Your account is created')
                return redirect('login')
        else:
            messages.info(request, 'Password did not matched')
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect("/")
            else:
                messages.info(request, 'Check username or password')
                return redirect('login')

    else:
        return render(request, 'login.html')


@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def upform(request):
    if request.method == 'Post':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm( request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'your account is updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form':u_form,
        'p_form': p_form,
    }
    return render(request,  'updateform.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')