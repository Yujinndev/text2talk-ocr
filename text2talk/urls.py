from django.urls import path 
from text2talk import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("", views.index, name="index"),
	path("textOcr/", views.image_to_text, name="textOcr"),
	path("talkOcr/", views.text_to_speech, name="talkOcr"),
	path("input/", views.text_input, name="input"),
	path("upload/", views.file_upload, name="upload"),
	path("live/", views.live_cam, name="live"),
	path("capture/", views.handle_video, name="capture"),
]

if settings.DEBUG:
    urlpatterns += static('/images/', document_root=settings.STATICFILES_DIRS[0])