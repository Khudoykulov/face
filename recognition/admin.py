from django.db import models
import base64
from django.utils.html import mark_safe
from django.contrib import admin
from .models import Person, Groups

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'face_image')

    def face_image(self, obj):
        if obj.face_img:  # face_img ni tekshirish
            # face_img - bu base64 formatidagi rasm, shuning uchun uni to'g'ri formatga aylantiramiz
            return mark_safe(f'<img src="data:image/jpeg;base64,{obj.face_img}" width="100" height="100" />')
        return "No Image"

    face_image.short_description = 'Face Image'

admin.site.register(Person, PersonAdmin)
admin.site.register(Groups) 