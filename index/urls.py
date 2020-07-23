from django.conf.urls import url
from . import views
# from django.urls import path, include

urlpatterns = [
	url(r'^/$', views.index, name='index'), # login url
	url(r'^account/dajsyewowq29aeqcv/$', views.account, name='account'),
	url(r'^signoff/$', views.logout, name='signoff'),
	# url('account/(?P<job>[A-Za-z]+)/$', views.dosomething, name='dosomething'),
]
