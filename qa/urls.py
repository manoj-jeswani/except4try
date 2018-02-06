from django.conf.urls import url
from .views import askView,qView,qdetailView,voteView


app_name="qa"

urlpatterns = [
	
	url(r'^ask/$',askView, name='ask'),
	url(r'^questions/$',qView, name='questions'),
	url(r'^qdetail/(?P<id>\d+)/$', qdetailView , name='qdetail'),
	url(r'^vote/$', voteView , name='vote'),
  
  


]

