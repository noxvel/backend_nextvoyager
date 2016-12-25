from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^movies/$', views.movie_list),
    url(r'^games/$', views.game_list),
    url(r'^item_create/$', views.item_create),
    url(r'^(item)/(?P<pk>[0-9]+)/$', views.item_detail),
]