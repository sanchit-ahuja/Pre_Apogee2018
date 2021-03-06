from django.conf.urls import url
from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^$', views.primary, name = 'primary'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^question/(?P<question_oder_no>[0-9]+)/$', views.question, name = 'question'),
    #url(r'^result/$', views.result, name = 'result'),
]
