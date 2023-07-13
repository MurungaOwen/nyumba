from django.contrib import admin
from .models import Houses,Like
# Register your models here.
@admin.register(Houses)
class HousesModelAdmin(admin.ModelAdmin):
    list_display=("category","rental_price","buying_price","location","uploaded")

@admin.register(Like)
class LikeModelAdmin(admin.ModelAdmin):
    list_display=("item","user")

    
    
