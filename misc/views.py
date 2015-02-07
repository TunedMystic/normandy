from django.shortcuts import render_to_response
from django.template import RequestContext

def errorHandler(request, template, status):
  response = render_to_response(template, context_instance=RequestContext(request))
  response.status_code = status
  return response

def handler404(request):
    return errorHandler(request, "misc/error404.html", 404)
  
def handler500(request):
    return errorHandler(request, 'misc/error500.html', 500)
