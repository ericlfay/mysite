from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    contents = models.TextField(verbose_name="正文")
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)