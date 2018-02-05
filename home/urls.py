from django.conf.urls import url
from .views import dashView
from django.contrib.auth import views as auth_views

app_name="home"

urlpatterns = [
	
	url(r'^$',dashView, name='dash'),

]
