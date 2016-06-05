from django.shortcuts import render
from rest_framework import viewsets

from jokes.models import Joke
from jokes.serializers import JokeSerializer


class JokeViewSet(viewsets.ModelViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
