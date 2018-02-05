from django.http import Http404
from django.shortcuts import render, redirect,get_object_or_404
from .forms import AskForm
from .models import Question
from users.models import Euser


def askView(request):
	if not request.user.is_authenticated:
		return redirect('users:login')


	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			print('form validated successfully')
			obj=form.save(commit=False)
			print(request.user.username)
			uobj=Euser.objects.get(username=str(request.user.username))
			print(form.cleaned_data['tag_list'])
			print(len(form.cleaned_data['tag_list']))
			obj.user=uobj
			obj.save()
			obj.tag_list.set(form.cleaned_data['tag_list'])
			
			return redirect("/")

	else:
		form = AskForm()


	return render(request, "qa/ask.html",{"form" : form,})


