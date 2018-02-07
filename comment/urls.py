from django.conf.urls import url
from .views import addCommentView


app_name="comment"

urlpatterns = [
	
	url(r'^add/(?P<is_cq>\d+)/(?P<pid>\d+)/$',addCommentView, name='add'),
	
   


]

