from django.db import models
import base64
import uuid


class Groups(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True, blank=True)
    face_encoding = models.BinaryField()
    face_img = models.TextField(null=True, blank=True)

    def get_face_image_base64(self):
        """Rasmni base64 formatida olish"""
        if self.face_img:
            return f"data:image/jpeg;base64,{self.face_img}"
        return None

    def __str__(self):
        return self.name