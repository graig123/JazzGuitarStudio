from django.conf.urls import url
from django.views.generic import TemplateView

#from views import ScalesPage

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='scales.html')),
]
