from django.urls import path, re_path
from app import views


urlpatterns = [
    path('', views.index, name='home'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('detect_mask_video_feed', views.mask_detect_feed, name='detect_mask_video_feed'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]
