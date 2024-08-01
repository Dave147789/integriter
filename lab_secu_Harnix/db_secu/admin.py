# admin.py

from django.contrib import admin
from .models import UploadedFile, UploadHistory

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('client', 'file', 'upload_time', 'hash_value')
    search_fields = ('user__username', 'file__name')  # Permet la recherche par nom d'utilisateur et nom de fichier

@admin.register(UploadHistory)
class UploadHistoryAdmin(admin.ModelAdmin):
    list_display = ('client','uploaded_file', 'hash_value')
    search_fields = ('user__username', 'uploaded_file__file__name')  # Permet la recherche par nom d'utilisateur et nom de fichier




