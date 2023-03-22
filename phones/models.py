from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=50, null=False, unique=True)
    image = models.ImageField()
    price = models.IntegerField(null=False)
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(editable=False, unique=True)

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)