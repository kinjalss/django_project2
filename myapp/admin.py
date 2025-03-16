from django.contrib import admin
from .models import Menu  # Import the Menu model

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Adjust fields as needed

