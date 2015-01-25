from fabric.api import local

def push(msg, remote = "origin", branch = "master"):
  local("git add -A")
  local("git commit -m '%s'" %(msg))
  local("git push %s %s" %(remote, branch))

def db(name = "db.sqlite3"):
  """
  Delete the (sqlite3) database and create a new one.
  """
  local("rm -rf %s" %(name))
  local("python manage.py makemigrations")
  local("python manage.py migrate")

def run(port = 8888):
  local("python manage.py runserver 0.0.0.0:%s" %(port))

def clean():     
  """Remove all the .pyc files"""
  local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)
