from django.shortcuts import render
from .models import Movie
from .serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status

# Create your views here.

class MovieView(APIView):
    def get(self, request, format = None):
        data = Movie.objects.all()
        serializer = MovieSerializer(data=data)
        return Response(serializer.data)