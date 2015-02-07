from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from tweets import views

urlpatterns = patterns('',
  #url(r"^/?$", TemplateView.as_view(template_name = "tweets/index.html"), name = "index"),
  url(r"^/?$", views.index, name = "index"),
  url(r"^api/users/$", views.UserList.as_view(), name = "user-list"),
  url(r"^api/users/(?P<pk>[0-9]+)$", views.UserDetail.as_view(), name = "user-detail"),
  url(r"^api/tweets/$", views.TweetList.as_view(), name = "tweet-list"),
  url(r"^api/tweets/(?P<pk>[0-9]+)$", views.TweetDetail.as_view(), name = "tweet-detail"),
  url(r'^api/token/$', obtain_auth_token),
)

"""
The obtain_auth_token view will return a JSON response when valid username and password fields are POSTed to the view using form data or JSON:

Example Request (Httpie):
  $ http --form POST http://127.0.0.1:8888/api/token/ username="drogo" password="drogo"

or

  $ http --json POST http://127.0.0.1:8888/api/token/ username="drogo" password="drogo"
  
Example Response: 
{                                                                                                                                                                             
    "token": "234eb70fad5bb4e7746fc444c1b249e0e7db2e49"                                                                                                                       
} 
"""

