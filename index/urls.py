# from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
	path('', views.index, name='index'), # login url
	path('account/dajsyewowq29aeqcv/', views.account, name='account'),
	path('signoff/', views.logout, name='signoff'),
	# url('account/(?P<job>[A-Za-z]+)/$', views.dosomething, name='dosomething'),
]
