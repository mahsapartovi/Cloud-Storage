from django.contrib import admin
from . import models
# Register your models here.


class FileUpload(admin.ModelAdmin):
    list_display = ('user', 'file', 'file_size')
    list_filter = ('user', "file_size")

admin.site.register(models.UserFiles, FileUpload)

