from django.http import Http404
from django.shortcuts import render, redirect,get_object_or_404
from qa.models import Category
def dashView(request):
    context={}
    return render(request,'home/dash.html',context)


def tagsView(request):
	cqset=Category.objects.all()

	context={'cqset':cqset,}
	return render(request,'home/tags.html',context)



def tagDetailView(request,id=None):
	cobj=get_object_or_404(Category,id=id)
	qset=cobj.question_set.all()
	context={'qset':qset,}
	return render(request,'qa/qlist.html',context)


