from fabric.api import local, task, warn_only

def service_database(action = "start"):
  """
  Run the database service.
  """
  with warn_only():
    # Database command line: psql
    if action == "stop":
      local("parts stop postgresql")
    else:
      local("parts start postgresql")

def service_redis(action = "start"):
  """
  Run the redis service.
  """
  with warn_only():
    # Redis command line: redis-cli
    if action == "stop":
      local("parts stop redis")
    else:
      local("parts start redis")

@task
def services(action = "start"):
  """
  Start/Stop all external services.
  """
  if action != "start":
    action = "stop"
  service_database(action)
  service_redis(action)

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
  local("honcho run python manage.py makemigrations")
  local("honcho run python manage.py migrate")

@task
def migratedb(role = "action", name = "webapp"):
  """
  Create a new postgres database.
  """
  with warn_only():
    local("psql -U %s -c 'CREATE DATABASE %s;'" %(role, name.lower()))
  local("honcho run python manage.py makemigrations")
  local("honcho run python manage.py migrate")

def deletedb(role = "action", name = "webapp"):
  """
  Drop postgres database.
  """
  with warn_only():
    local("psql -U %s -c 'DROP DATABASE %s;'" %(role, name.lower()))

@task 
def gresdb(role = "action", name = "webapp"):
  """
  Delete a postgres database and create a new one.
  """
  deletedb(role = role, name = name.lower())
  migratedb(role = role, name = name.lower())

@task
def django_server():
  """
  Run the Django dev server.
  """
  services("start")
  local("python manage.py runserver 0.0.0.0:$PORT")

@task
def gunicorn_server():
  """
  Run the Gunicorn web server.
  """
  services("start")
  local("gunicorn --bind 0.0.0.0:$PORT webapp.wsgi")

@task
def clean():     
  """Remove all the .pyc files"""
  local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)

@task
def run():
  """
  Run the Django dev server.
  """
  local("honcho run fab django_server")

@task
def gun():
  """
  Run the Gunicorn web server.
  """
  local("honcho run fab gunicorn_server")
