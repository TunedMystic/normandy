from celery.task.schedules import crontab
from celery.decorators import periodic_task
from datetime import datetime
from tweets.models import Tweet

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute = "*", day_of_week = "*")))
def greet():
  count = Tweet.objects.count()
  recent = Tweet.objects.all()[:5]
  print "\n\n"
  print "There are currently %d number of tweets." %(count)
  print "The most recent tweets are:"
  print "\n".join(str(twt) for twt in recent)
  print "\n\n"