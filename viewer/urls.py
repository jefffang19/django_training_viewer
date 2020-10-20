from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_training', views.send_training, name = 'send_training'),
    path('get_training', views.get_training, name = 'get_training'),
    path('del_everything', views.del_everything, name = 'del_everything'),
]
