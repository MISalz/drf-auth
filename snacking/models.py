from django.db import models
from django.contrib.auth import get_user_model
	
class Snacking(models.Model):
  owner = models.CharField(max_length=256)
  name = models.CharField(max_length=256)
  description = models.CharField(max_length=256)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
