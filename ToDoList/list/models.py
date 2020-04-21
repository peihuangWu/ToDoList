from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="标题", default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者", null=True, blank=True)
    publish_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    content = models.TextField(default="", verbose_name="内容")

    class Meta:
        verbose_name = "任务信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

