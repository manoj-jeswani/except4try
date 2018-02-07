from django.conf.urls import url
from django.views.generic import TemplateView
app_name="api_doc"


urlpatterns = [

	url(r'^links$', TemplateView.as_view(template_name="api_doc/links.html", content_type="text/html"), name="api-doc-links")


]