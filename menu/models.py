from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True,
                               related_name='sub_menu', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
