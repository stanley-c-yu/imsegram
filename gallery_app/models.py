from django.db import models
from django.utils.safestring import mark_safe # new
from PIL import Image as Im # new

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    photo = models.ImageField(upload_to='pics') # the upload_to='pics' tells Django to store the photo in a directory called pics under the media directory.  If you see a missing directory error, add it manually.  


    def image_tag(self): # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.photo)) 