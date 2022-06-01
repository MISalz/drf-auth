from .models import Snacking
from django.contrib import admin
		
admin.site.register(Snacking)
#adds names to items in db

def __str__(self):
      return self.name