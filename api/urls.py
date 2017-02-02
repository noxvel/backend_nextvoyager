from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^item_list/(?P<kind>(movie|game))/$', views.ItemList.as_view()),
    url(r'^item/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
    url(r'^item/(?P<item_pk>[0-9]+)/review/$', views.ReviewList.as_view()),
    url(r'^item/(?P<item_pk>[0-9]+)/review/(?P<pk>[0-9]+)/$', views.ReviewDetail.as_view()),
    url(r'^user/', views.UserListView.as_view()),
    url(r'^api-auth/', obtain_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)