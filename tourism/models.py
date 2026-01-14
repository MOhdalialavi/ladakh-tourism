from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)   # like leh, kargil, pangong-lake
    description = models.TextField()
    
    culture = models.TextField(blank=True)
    ethnicity = models.TextField(blank=True)
    best_time = models.CharField(max_length=200, blank=True)
    how_to_reach = models.TextField(blank=True)

    image = models.ImageField(upload_to='places/', blank=True, null=True)

    def __str__(self):
        return self.name
