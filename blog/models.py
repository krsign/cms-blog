from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Post(models.Model):
    statuses = [('D', 'Draft'), ('P', 'Publish')]

    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.CharField(max_length=1 ,choices=statuses, default='D')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    image = models.ImageField(upload_to='blog/', blank=True)
    slug = models.SlugField(unique=True, blank=True)

    # we want unique slug_
    # django provides slugify - slugify(value) => will create slug 
    # in our case value = title

    def __str__(self):
        return self.title

    # whenever you save data in model django will call this method
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        try:
            super().save(*args, **kwargs)
        except:
            pass

