
from django.urls import path
from django.conf import settings
from django.conf.urls import static
from .views import MovieView
from django.conf.urls.static import static
urlpatterns = [
    path('',MovieView.as_view(),name='movie'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
