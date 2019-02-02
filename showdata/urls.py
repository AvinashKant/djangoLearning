from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
path('', views.index, name='showdataindex'),
path('second', views.sindex, name='showdat'),
path('login', TemplateView.as_view(template_name = 'login.html'),name='showdatalogin'),
path('submitform',views.login,name='submitabc'),
path('login2', views.login2html,name='login2htmlview'),
path('login2form',views.testLogin,name='login2'),
]