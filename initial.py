#!/usr/bin/env python
import os
import sys
import uuid
import datetime
import random
import arrow
import django

# Clear the database.
def endall():
  # Delete Users.
  for obj in get_user_model().objects.all():
    obj.delete()

# Make User object.
def makeUser(n, e, p):
  try:
    usr = get_user_model().objects.get(username = n)
    return usr
  except get_user_model().DoesNotExist:
    return get_user_model().objects.create_user(username = n, email = e, password = p)

# Make a random date.
def randomDate():
  """
  This function will return a random datetime between two datetime objects.
  """
  start = arrow.get(datetime.datetime(2014, 7, 1, 12, 0, 0))
  end = arrow.get(datetime.datetime(2014, 12, 17, 12, 0, 0))
  delta = end - start
  int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
  random_second = random.randrange(int_delta)
  d = start + datetime.timedelta(seconds=random_second)
  return arrow.get(d).datetime

# Return a random User.s
randomUser = lambda: get_user_model().objects.all()[random.randrange(0, get_user_model().objects.count())]

# Make a random Url.
randomUrl = lambda: str(uuid.uuid4())[:6]

def main():
  
  # Make Users.
  print "\nMaking Users..."
  makeUser("Harry", "harry@gmail.com", "harry101")
  makeUser("Natalie", "natalie@gmail.com", "natalie101")
  makeUser("Ramin", "ramin@gmail.com", "ramin101")
  makeUser("Tyler", "tyler@gmail.com", "tyler101")
  makeUser("Bella", "bella@gmail.com", "bella101")
  makeUser("Blossom", "blossom@gmail.com", "blossom101")
  makeUser("Starbuck", "starbuck@gmail.com", "starbuck101")
  makeUser("Chewbacca", "chewbacca@gmail.com", "chewbacca101")
  makeUser("Vader", "vader@gmail.com", "vader101")
  makeUser("Obi-wan", "obiwan@gmail.com", "obiwan101")
  Drogo = get_user_model().objects.create_superuser(username = "drogo", email = "drogo@gmail.com", password = "drogo101")
  Anakin = get_user_model().objects.create_superuser(username = "anakin", email = "anakin@gmail.com", password = "anakin101")
  print "[Done] Making Users."
  
  print "\nMaking Fake <Tweet>s..."
  # Generate fake models.
  # https://github.com/joke2k/django-faker
  populator = Faker.getPopulator()
  populator.addEntity(Tweet, 20, {
      "user": lambda x: randomUser()
  })
  generatedModels = populator.execute()
  print "[Done] Making Fake <Tweet>s."
  

if __name__ == "__main__":
  from getenv import env
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{0}'.format(env('DJANGO_SETTINGS_MODULE')))
  django.setup()
  from django.contrib.auth import get_user_model
  from django_faker import Faker
  from tweets.models import Tweet
  
  if 'x' in sys.argv[1:]:
    print "Clearing database...\n"
    endall()
  
  main()

