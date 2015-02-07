from fabric.api import local, task, warn_only

@task
def push(msg, remote = "origin", branch = "master"):
  """
  Git add, git commit, and git push.
  """
  local("git add -A")
  local("git commit -m '%s'" %(msg))
  local("git push %s %s" %(remote, branch))

@task
def db(name = "db.sqlite3"):
  """
  Delete the (sqlite3) database and create a new one.
  """
  local("rm -rf %s" %(name))
  local("python manage.py makemigrations")
  local("python manage.py migrate")

@task
def createdb(role = "action", name = "webapp", s = "p"):
  """
  Create a new postgres database.
  """
  with warn_only():
    local("psql -U %s -c 'CREATE DATABASE %s;'" %(role, name.lower()))
  django_settings = "--settings=webapp.settings.dev"
  if s == "p":
    django_settings = "--settings=webapp.settings.prod"
  local("python manage.py makemigrations %s" %(django_settings))
  local("python manage.py migrate %s" %(django_settings))

@task
def deletedb(role = "action", name = "webapp"):
  """
  Drop postgres database.
  """
  with warn_only():
    local("psql -U %s -c 'DROP DATABASE %s;'" %(role, name.lower()))

@task 
def gresdb(role = "action", name = "webapp", s = "p"):
  """
  Delete a postgres database and create a new one.
  """
  deletedb(role = role, name = name.lower())
  createdb(role = role, name = name.lower(), s = s)

@task
def run(port = 8888):
  """
  Run the Django dev server.
  """
  local("python manage.py runserver 0.0.0.0:%s --settings=webapp.settings.dev" %(port))

@task
def runp(port = 8888):
  """
  Run the Django server with production settings.
  """
  local("python manage.py runserver 0.0.0.0:%s --settings=webapp.settings.prod" %(port))

@task
def gun(host = "0.0.0.0", port = "8888"):
  """
  Run Gunicorn web server.
  """
  local("gunicorn -b %s:%s --env DJANGO_SETTINGS_MODULE=webapp.settings.dev webapp.wsgi" %(host, port))

@task
def gunp(host = "0.0.0.0", port = "8888"):
  """
  Run Gunicorn web server with production settings.
  """
  local("gunicorn -b %s:%s --env DJANGO_SETTINGS_MODULE=webapp.settings.prod webapp.wsgi" %(host, port))

@task
def clean():     
  """Remove all the .pyc files"""
  local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)
