from django.db import models

# Create your models here.
class Todo(models.Model):
  body = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.body[:20]

