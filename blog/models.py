from django.db import models
from django.contrib.auth import get_user_model

import markdown

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="类型名")

    class Meta:
        verbose_name = "类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="标签名")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    contents = models.TextField(verbose_name="正文")
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    excerpt = models.CharField(max_length=200, blank=True, verbose_name="摘要")
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    goods = models.PositiveIntegerField(default=0, verbose_name="点赞量")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    
    def save(self, *args, **kwargs):
        if not self.excerpt:

            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Blog, self).save(*args, **kwargs)


class Comment(models.Model):
    name = models.TextField(verbose_name="评论")
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    goods = models.PositiveIntegerField(default=0, verbose_name="点赞量")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
