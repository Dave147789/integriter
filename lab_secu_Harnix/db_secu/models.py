# db_secu/models.py

# db_secu/models.py
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User,Group
import os
import hashlib


#TABLE ACCETANT TOUS LES DONNES
class UploadedFile(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to=~models.Q(groups__name__in=['Interne']) & ~models.Q(is_staff=True))
    file = models.FileField(upload_to='uploaded_files/%Y/%m/%d/',validators=[FileExtensionValidator(['txt'])])
    upload_time = models.DateTimeField(auto_now_add=True)
    hash_value = models.CharField(max_length=64, null=True, blank=True)

    def calculate_hash(self):
        if self.file:
            file_path = self.file.path
            if os.path.exists(file_path):
                sha256_hash = hashlib.sha256()
                with open(file_path, "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                return sha256_hash.hexdigest()
        return None

    def __str__(self):
        return f'{self.client.username} - {self.file.name}'


#TABLE ACCETANT QUE LES DONNNES DE SOURc
class UploadHistory(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    hash_value = models.CharField(max_length=64, null=True, blank=True)



