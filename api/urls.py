from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^movies/$', views.movie_list),
    url(r'^games/$', views.game_list),
    url(r'^(movies|games)/(?P<pk>[0-9]+)/$', views.item_detail),
]