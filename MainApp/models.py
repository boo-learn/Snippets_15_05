from django.db import models
from django.contrib.auth.models import User

LANGS = (
    ("py", "python"),
    ("js", "JavaScript"),
    ("cpp", "C++"),
)


class Language(models.Model):
    name = models.CharField(max_length=32)
    # icon = ...
    # shot_name = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.name}"


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    # lang = models.CharField(max_length=30, choices=LANGS)
    lang = models.ForeignKey(to=Language, on_delete=models.PROTECT,
                             null=True, blank=True)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True, related_name='snippets')
    private = models.BooleanField(default=True)
    # likes = models.ManyToManyField(to=User)
    # dislikes = models.ManyToManyField(to=User)

    def __str__(self):
        return f"Snippet {self.name} | {self.user}"


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, related_name='comments')
