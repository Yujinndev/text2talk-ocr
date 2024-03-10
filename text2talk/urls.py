from django.urls import path 
from text2talk import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("", views.index, name="index"),
	path("textOcr/", views.image_to_text, name="textOcr"),
	path("talkOcr/", views.text_to_speech, name="talkOcr")
	# path("live/", views.video_feed, name="live"),
]

if settings.DEBUG:
    urlpatterns += static('/images/', document_root=settings.STATICFILES_DIRS[0])