from fabric.api import local

def push(msg, remote = "origin", branch = "master"):
  local("git add -A")
  local("git commit -m '%s'" %(msg))
  local("git push %s %s" %(remote, branch))

def run(port = 8888):
  local("python manage.py runserver 0.0.0.0:%s" %(port))

def clean():     
  """Remove all the .pyc files"""
  local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)
