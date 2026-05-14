from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название тега")

    def __str__(self):
        return self.name

class ProjectGoal(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название цели")
    description = models.TextField(verbose_name="Описание")
    priority = models.IntegerField(default=1, verbose_name="Приоритет")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to='goals/', blank=True, null=True, verbose_name="Изображение")
    tags = models.ManyToManyField(Tag, blank=True, related_name='goals', verbose_name="Теги")

    def __str__(self):
        return self.name

class Comment(models.Model):
    goal = models.ForeignKey(ProjectGoal, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} - {self.goal.name}"