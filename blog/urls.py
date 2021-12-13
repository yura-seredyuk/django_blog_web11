from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<pk>[0-9]+)$', views.post_details, name='post_details'),
    # path('post/<int:pk>',views.post_details, name='post_details'),
    url(r'^post/(?P<pk>[0-9]+)/delete$', views.post_delete, name='post_delete'),
    url(r'^post/create$', views.post_create, name='post_create'),
    url(r'^post/(?P<pk>[0-9]+)/edit$', views.post_edit, name='post_edit'),
    url(r'^login$', views.user_login, name='login'),
]