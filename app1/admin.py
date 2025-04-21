from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # fieldsetsga qo'shimcha maydonlarni qo'shish
    model_fields = [field.name for field in User._meta.get_fields()]
    print()
    fieldsets = UserAdmin.fieldsets + (
        ("Qo'shimcha rollar", {
            "fields": tuple(model_fields[12:-2]),  # Maydonlar nomlari bilan ishlang
        }),
    )

    # Ro'yxatdagi ko'rinadigan ustunlar
    list_display = (
        "username", "email", "first_name", "last_name", 
        "is_admin", "is_teacher", "is_student", "is_parent", "is_staff"
    )
    
    # Yon panel uchun filtrlar
    list_filter = ("is_admin", "is_teacher", "is_student", "is_parent", "is_staff", "is_active")
    
    # Qidiruv qatorida ishlatiladigan ustunlar
    search_fields = ("username", "email", "first_name", "last_name")

# Custom User modelini admin panelga qo'shish
admin.site.register(User, CustomUserAdmin)

# Register your models here.
