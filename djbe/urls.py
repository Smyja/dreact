from django.urls import path,re_path
from djbe import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('', views.home, name='home'),
    
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
]
