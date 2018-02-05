from django.conf.urls import url
from .views import askView


app_name="qa"

urlpatterns = [
	
	url(r'^ask/$',askView, name='ask'),
  
]

