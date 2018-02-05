from django.http import Http404
from django.shortcuts import render, redirect,get_object_or_404

def dashView(request):
    context={}
    return render(request,'home/dash.html',context)