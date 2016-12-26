from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^item_list/(?P<kind>(movie|game))/$', views.ItemList.as_view()),
    url(r'^item/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
    url(r'^item/(?P<item_pk>[0-9]+)/review/$', views.ReviewList.as_view()),
    url(r'^item/(?P<item_pk>[0-9]+)/review/(?P<pk>[0-9]+)/$', views.ReviewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)