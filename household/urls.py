from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='household/index.html')),
    url(r'^today/$', TemplateView.as_view(template_name='household/today.html'), name='today'),
]
