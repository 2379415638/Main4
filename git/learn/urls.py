from django.conf.urls import url, include
from . import views

urlpatterns = [

	url(r'^$', views.index, name = "index"),
	url(r'^login/',views.login,name = "login"),
	url(r'^logout/',views.logout,name="logout"),
	url(r'^contact/$',views.contact,name="contact"),
	url(r'^user/$',views.user,name="user"),
	url(r'^advice/$',views.advice,name="advice"),
	url(r'^email/(.*?)/$',views.email,name="email"),
]