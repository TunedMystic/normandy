from django.db import models
from django.conf import settings

class Tweet(models.Model):
  """
  A simple tweet model.
  """
  user = models.ForeignKey(settings.AUTH_USER_MODEL, unique = True)
  text = models.CharField(max_length = 140, blank = False)
  timestamp = models.DateTimeField(auto_now_add = True)
  
  def __unicode__(self):
    return "%s:%s" %(self.user.username[:24], self.text[:24])
