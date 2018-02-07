from django.http import Http404

from django.contrib.auth import views as auth_views

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import auth
from .forms import EuserRegisterForm
from .models import Euser



def registerView(request):
	if request.method == 'POST':
		form = EuserRegisterForm(request.POST)
		if form.is_valid():
			print('form validated successfully')
			user = form.save()
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user.set_password(password)
			user.save()
			new_user = auth.authenticate(username=username, password=password)
			if new_user is not None:
				auth.login(request, new_user)
				print("yooo")
			return redirect("/")

	else:
		form = EuserRegisterForm()


	return render(request, "users/register.html",{"form" : form,})





def login(request, **kwargs):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return auth_views.login(request, **kwargs)


def profileView(request,id=None):
	uobj=get_object_or_404(Euser,id=id)
	return render(request, "users/profile.html",{"uobj" : uobj,})



def allUsersView(request):
	uqset=Euser.objects.all()
	return render(request, "users/ulist.html",{"uqset" : uqset,})
 