from django.conf.urls import url
from .views import registerView,login
from django.contrib.auth import views as auth_views





app_name="users"

urlpatterns = [
	
	url(r'^register/$',registerView, name='register'),
	url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'users/logout.html'}, name='logout'),
    
]
