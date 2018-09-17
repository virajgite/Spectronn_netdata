 
from django.conf.urls import url,include

from . import views

urlpatterns = [

        url(r'^$',views.index,name='index'),
	url(r'^historic',views.historic,name='historic'),
	url(r'^pie',views.pie,name='pie'),
]

