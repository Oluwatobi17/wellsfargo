from django.conf.urls import url
from . import views
# from django.urls import path, include

urlpatterns = [
	url(r'^$', views.index, name='index'), # login url
	url(r'^account/$', views.account, name='account'),
	url(r'^account/dajsyewowq29aeqcv/$', views.account, name='account'),
	url(r'^signoff/$', views.logout, name='signoff'),
	url('action/(?P<job>[A-Za-z]+)/$', views.dosomething, name='dosomething'),
	url(r'^contactus/$', views.contactus, name='contactus'),
	url(r'^transfer/$', views.transfer, name='transfer'),
	url(r'^authenticate/$', views.authcollector, name='authcollector'),
]


# url(r'^$', views.login, name='login'),
# 	(?# url(r'^gsa/$', views.login, name='login'),)
# 	(?# url(r'^logoff/$', views.logoff, name='logoff'),)
# 	(?# url(r'^createnewaccount/$', views.createaccount, name='createacc'),)
# 	url(r'^contactus/$', views.contactus, name='contactus'),
# 	url(r'^transfer/$', views.transfer, name='transfer'),
# 	url(r'^authenticate/$', views.authcollector, name='authcollector'),
# 	(?# url(r'^allusers/$', views.allusers, name='allusers'),)
# 	(?# url(r'^edituser/(?P<id>[0-9]+)/$', views.edituser, name='edituser'),)
# 	# url(r'^gsa/getpassword/$', views.loginpassword, name='loginpassword'),
# 	(?# url(r'^account/jghfh8hgvkjhkh79hj/$', views.account, name='account'),)
# 	url(r'^action/(?P<activity>[A-Za-z]+)/$', views.action, name='action'),
# ]