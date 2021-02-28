from django.db import models
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_contact', args=[str(self.id)])

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '../../static/images/profile.png'
        return url
