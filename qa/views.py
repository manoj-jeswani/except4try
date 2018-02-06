from django.http import Http404,HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .forms import AskForm,AnsForm
from .models import Question,Answer
from users.models import Euser
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


import json

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
			return redirect(reverse('qa:questions'))

	else:
		form = AskForm()


	return render(request, "qa/ask.html",{"form" : form,})

def ansView(request,id=None):
	if not request.user.is_authenticated:
		return redirect('users:login')


	if request.method == 'POST':
		form = AnsForm(request.POST)
		if form.is_valid():
			print('form validated successfully')
			obj=form.save(commit=False)
			print(request.user.username)
			uobj=Euser.objects.get(username=str(request.user.username))
			obj.user=uobj
			obj.save()
			qobj=get_object_or_404(Question,id=id)
			qobj.ans_list.add(obj)
			return redirect(reverse('qa:qdetail', args=[id]))


	else:
		form = AnsForm()


	return render(request, "qa/ans.html",{"form" : form,})







def qView(request):
	qset=Question.objects.all()

	return render(request, "qa/qlist.html",{"qset" : qset,})




def qdetailView(request,id=None):
	
	qobj=get_object_or_404(Question,id=id)


	return render(request, "qa/qdetail.html",{"qobj" : qobj,})





@csrf_exempt
def voteView(request):
	
	if request.is_ajax() and  all([x in request.POST.keys() for x in  ('is_q','id','is_up')]):
		if not request.user.is_authenticated:
			data={'new_votes':None,'done':False,'msg':'You must be logged in to vote!'}
		else:

			is_q=int(request.POST['is_q'])
			id=int(request.POST['id'])
			is_up=int(request.POST['is_up'])
			if is_q:
				obj=Question.objects.get(id=id)
			else:
				obj=Answer.objects.get(id=id)			

			if obj.user.username==request.user.username:
				data={'new_votes':None,'done':False,'msg':"You can't vote your own content!"}
				
			else:
				eobj=get_object_or_404(Euser,username=request.user.username)	
				if is_up:
					if eobj in obj.upvoters.all():
						obj.votes=obj.votes-1
						obj.upvoters.remove(eobj)

					elif eobj in obj.downvoters.all():
						pass

					else:	
						obj.votes=obj.votes+1
						obj.upvoters.add(eobj)

				else:
					if eobj in obj.downvoters.all():
						obj.votes=obj.votes+1
						obj.downvoters.remove(eobj)

					elif eobj in obj.upvoters.all():
						pass
					else:	
						obj.votes=obj.votes-1
						obj.downvoters.add(eobj)

				obj.save()
				data={'new_votes':obj.votes,'done':True,'msg':'Voted successfully'}
			
	else:
		# 'This is not an ajax request or invalid data'
		data=False
	
	return HttpResponse(json.dumps(data), content_type ='application/json; charset=utf8')

