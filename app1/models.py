from django.db import models
from django.contrib.auth.models import AbstractUser
from recognition.models import Person
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_admin = models.BooleanField(default=False, help_text="Foydalanuvchi admin ekanligini bildiradi", verbose_name="Admin")
    is_teacher = models.BooleanField(default=False, help_text="Foydalanuvchi o'qituvchi ekanligini bildiradi", verbose_name="O'qituvchi")
    is_student = models.BooleanField(default=True, help_text="Foydalanuvchi talaba ekanligini bildiradi", verbose_name="Talaba")
    is_parent = models.BooleanField(default=False, help_text="Foydalanuvchi ota-ona ekanligini bildiradi", verbose_name="Ota-ona")
    face_date = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, help_text="Shaxsning yuz ma'lumotlariga ishora", verbose_name="Yuz Ma'lumotlari")
