from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django import template
from django.http.response import StreamingHttpResponse

from .camera import VideoCamera
from .detect_mask_camera import DetectMaskCamera


# Create your views here.
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))

def pages(request):
  context = {}
  try:
    load_template = request.path.split('/')[-1]
    context['segment'] = load_template

    html_template = loader.get_template(load_template) 
    return HttpResponse(html_template.render(context, request))
      
  except template.TemplateDoesNotExist:
    html_template = loader.get_template( 'page-404.html' )
    return HttpResponse(html_template.render(context, request))

  except:
    html_template = loader.get_template( 'page-500.html' )
    return HttpResponse(html_template.render(context, request))

def gen(camera):
  while True:
      frame = camera.get_frame()
      yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
  return StreamingHttpResponse(gen(VideoCamera()),
          content_type='multipart/x-mixed-replace; boundary=frame')

def mask_detect_feed(request):
  return StreamingHttpResponse(gen(DetectMaskCamera()),
          content_type='multipart/x-mixed-replace; boundary=frame')