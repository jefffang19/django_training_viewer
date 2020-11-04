from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_training', views.send_training, name = 'send_training'),
    path('get_training', views.get_training, name = 'get_training'),
    path('del_everything', views.del_everything, name = 'del_everything'),
    path('view_loss', views.view_loss, name = 'view_loss'),
    path('view_acc', views.view_acc, name = 'view_acc'),
]
