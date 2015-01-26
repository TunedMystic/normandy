import logging
from django.shortcuts import render
from tweets.models import Tweet

logger = logging.getLogger(__name__)

def index(request):
  logger.debug("Hitting the index view..")
  stuff = Tweet.objects.all()[:10]
  return render(request, "tweets/index.html", {"stuff": stuff})
