from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from tweets import views

urlpatterns = patterns('',
  #url(r"^/?$", TemplateView.as_view(template_name = "tweets/index.html"), name = "index"),
  url(r"^/?$", views.index, name = "index"),
  url(r"^api/users/$", views.UserList.as_view(), name = "user-list"),
  url(r"^api/users/(?P<pk>[0-9]+)$", views.UserDetail.as_view(), name = "user-detail"),
  url(r"^api/tweets/$", views.TweetList.as_view(), name = "tweet-list"),
  url(r"^api/tweets/(?P<pk>[0-9]+)$", views.TweetDetail.as_view(), name = "tweet-detail"),
)
