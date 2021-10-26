from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.feed_image)
admin.site.register(models.likes)
admin.site.register(models.comments)