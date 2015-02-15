from celery.task.schedules import crontab
from celery.decorators import periodic_task
from datetime import datetime

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute = "*", day_of_week = "*")))
def greet():
  print "\n***---***---***---***---***---***---***"
  print "Hello from Celery!"
  print "It is now", datetime.now().strftime("%a %b %d %Y @ %I:%M:%S %p")
  print "***---***---***---***---***---***---***\n"