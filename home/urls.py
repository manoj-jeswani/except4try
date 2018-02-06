from django.conf.urls import url
from .views import dashView,tagsView,tagDetailView
from django.contrib.auth import views as auth_views

app_name="home"

urlpatterns = [
	
	url(r'^$',dashView, name='dash'),
	url(r'^tags/$',tagsView, name='tags'),
	url(r'^tag_detail/(?P<id>\d+)/$', tagDetailView , name='tag_detail'),
	

]
