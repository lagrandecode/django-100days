
from django.urls import path
from django.conf import settings
from django.conf.urls import static
from .views import MovieView
urlpatterns = [
    path('',MovieView.as_view(),name='movie'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
