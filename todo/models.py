from django.db import models

# Create your models here.
class TodoModel(models.Model):
    body = models.CharField(max_length=60)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)

    class Meta:
        ordering = ['-id']
