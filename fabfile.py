from fabric.api import local, task

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
def run(port = 8888):
  """
  Run the Django dev server.
  """
  local("python manage.py runserver 0.0.0.0:%s" %(port))

@task
def prod(port = 8888):
  """
  Run the Django server with production settings.
  """
  local("python manage.py runserver 0.0.0.0:%s --settings=webapp.settings.prod" %(port))

@task
def gun(host = "0.0.0.0", port = "8888"):
  """
  Run Gunicorn web server.
  """
  local("gunicorn -b %s:%s webapp.wsgi" %(host, port))

@task
def clean():     
  """Remove all the .pyc files"""
  local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)
