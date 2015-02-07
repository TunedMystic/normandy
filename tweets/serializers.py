from rest_framework import serializers
from tweets.models import Tweet
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  tweet_set = serializers.HyperlinkedRelatedField(
    many = True,
    read_only = True,
    view_name = "tweet-detail"
  )
  
  class Meta:
    model = User
    fields = ("username", "email", "tweet_set")


class TweetSerializer(serializers.ModelSerializer):
  #user = serializers.ReadOnlyField(source = "user.username")
  user = serializers.HyperlinkedRelatedField(
    view_name = "user-detail",
    read_only = True
  )
  
  class Meta:
    model = Tweet
    fields = ("url", "user", "text", "timestamp")