from django.conf.urls import url
from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'


urlpatterns = [
    # path('', views.index, name='index'), #no need to mention becouse direct connect
    path('',views.basic,name='basic'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),

]
