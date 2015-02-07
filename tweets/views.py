import logging
from django.shortcuts import render
from django.contrib.auth import get_user_model
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
  queryset = User.objects.all()
  serializer_class = UserSerializer


class TweetList(ListCreateAPIView):
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer


class TweetDetail(RetrieveAPIView):
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer
