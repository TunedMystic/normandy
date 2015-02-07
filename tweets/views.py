import logging
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from tweets.models import Tweet
from tweets.serializers import TweetSerializer, UserSerializer

User = get_user_model()

logger = logging.getLogger(__name__)

def index(request):
  logger.debug("Hitting the index view..")
  stuff = Tweet.objects.all()[:10]
  return render(request, "tweets/index.html", {"stuff": stuff})


class UserList(ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
  """
  Note: ('authentication_classes' and 'permission_classes') must
  be set in order to enable authentication on a view(s).
  This view is an example of Token authentication.
  Failing to provide an auth token will result in a 401 unauthorized error.
  
  Httpie usage:
    $ http GET localhost:8888/api/users/1 "Authorization:Token 234eb70fad5bb4e7746fc444c1b249e0e7db2e49"
  .
  .
  """
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  queryset = User.objects.all()
  serializer_class = UserSerializer


class TweetList(ListCreateAPIView):
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer


class TweetDetail(RetrieveAPIView):
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer
