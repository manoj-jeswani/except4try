from django.conf.urls import url
from .views import askView,qView,qdetailView,voteView,ansView


app_name="qa"

urlpatterns = [
	
	url(r'^ask/$',askView, name='ask'),
	url(r'^questions/$',qView, name='questions'),
	url(r'^qdetail/(?P<id>\d+)/$', qdetailView , name='qdetail'),
	url(r'^vote/$', voteView , name='vote'),
	url(r'^ans/(?P<id>\d+)/$', ansView , name='ans'),
  
  


]

