from __future__ import unicode_literals

from django.db import models

class Joke(models.Model):
    question = models.TextField()
    punchline = models.TextField()
    laughs = models.PositiveIntegerField(default=0)
