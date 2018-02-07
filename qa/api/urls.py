from django.conf.urls import url
from .views import *

app_name="qa-api"


urlpatterns = [

	url(r'^all_questions/$', QuestionList.as_view(), name='all_questions'),
	url(r'^answers/(?P<qid>\d+)/$', AnswerList.as_view(), name='answers'),
	url(r'^ask_question/$', AskQuestion.as_view(), name='ask_question'),
		
]