from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
# from django.utils.http import is_safe_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


def login_view(request):
    msg=None
    userlogin = request.user
    # print(userlogin.id)
    if request.method == "POST":
        username_var = request.POST.get('username')
        password_var = request.POST.get('password')
        user = authenticate(request,username=username_var, password=password_var)

        qs = User.objects.filter(username=username_var)
        if len(qs) < 1:
            msg = 'This user does not EXIST!'
        
        try:
            user = User.objects.get(username=username_var)
        except:
            user = None
        if user is not None and not user.check_password(password_var):
            msg = 'Wrong Password'
        elif user is None:
            pass
        else:     
            login(request, user)
            # messages.success(request, "Welcome" + " " + str(userlogin))
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect("/profiles")

    context = {"msg":msg}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    # messages.success(request, "Sad to see you leave! See you soon please!")
    return HttpResponseRedirect('%s'%(reverse("auth_login")))

