from django.contrib import admin
from .models import Image
# Register your models here.
class imageAdmin(admin.ModelAdmin):
    """
    The list_display list tells Django admin to display its contents in the admin dashboard. The contents are the model’s fields.
    
    In this case, we want it to display the title and photo fields of every image that is uploaded.
    """
    list_display = ["title", "image_tag", "photo"]

admin.site.register(Image, imageAdmin)