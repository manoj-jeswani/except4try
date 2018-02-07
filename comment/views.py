from django.shortcuts import render
from .forms import CommentForm
import json
from django.http import HttpResponse
from qa.models import Question,Answer
from users.models import Euser
# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.http import Http404


def addCommentView(request,is_cq=None,pid=None):
	if not request.user.is_authenticated:
		response = {}
		if request.is_ajax():
			response['valid']=False
			response['message'] = "You must be logged in to submit the comment."
			response['ctext'] =""
		else:
			raise Http404("User not found! Login to continue")

	else:

		if request.method=='POST':
			response = {}
			
			f=CommentForm(request.POST)
			if f.is_valid():
				cobj=f.save(commit=False)
				if int(is_cq):
					qobj=get_object_or_404(Question,id=pid)
					cobj.que=qobj
				else:
					aobj=get_object_or_404(Answer,id=pid)
					cobj.ans=aobj
				uobj=Euser.objects.get(username=str(request.user.username))
				cobj.user=uobj
				cobj.save()

				if request.is_ajax():
					response['valid']=True
					response['message'] = "Comment added."
					response['ctext'] = cobj.comment

			else:
				if request.is_ajax():
					response['valid']=False
					response['message'] = "Unable to submit, verify and submit again.. "
					response['ctext'] =""
		else:
			if request.is_ajax():
				response['message'] = "(GET request)"


	return HttpResponse(json.dumps(response), content_type ='application/json; charset=utf8')




