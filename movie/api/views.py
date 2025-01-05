from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status

# Create your views here.

class MovieView(APIView):
    def get(self, request, format = None):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data)
    def post(self, request,format = None):
        movie = Movie.objects.all()
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)ß