from django.urls import path

from www import views

urlpatterns = [
    path('upload', views.upload_form, name='upload'),
    path('tip', views.tip_form, name='tip'),
    path('list', views.im_list, name='list'),
    path('acc_list', views.acc_list, name='acc_list'),

]
