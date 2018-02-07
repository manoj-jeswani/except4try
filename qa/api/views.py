from rest_framework import generics
from rest_framework import permissions
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404,Http404
from qa.models import Question

class QuestionList(generics.ListAPIView):
   
    serializer_class = AllQuestionsSerializer

    def get_queryset(self):
        return Question.objects.all()




class AnswerList(generics.ListAPIView):
  
	serializer_class = AllAnswersSerializer
	lookup_url_kwarg="qid"

	def get_queryset(self):
		qobj=get_object_or_404(Question,id=self.kwargs['qid'])
		return qobj.ans_list.all()


class AskQuestion(generics.ListCreateAPIView):
   
    serializer_class = AllQuestionsSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_queryset(self):
        return Question.objects.all()


