from django.db import models

class ProjectGoal(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название цели")
    
    description = models.TextField(verbose_name="Описание")
    
    priority = models.IntegerField(default=1, verbose_name="Приоритет")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name