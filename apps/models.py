from django.db import models
from django.db.models import CharField, ImageField, DecimalField, DateTimeField, DateField, TextField, SlugField
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Packages(models.Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='media/package_images',
                       blank=True,
                       null=True)
    cost = DecimalField(max_digits=10, decimal_places=2)
    description = CKEditor5Field('Text', config_name='extends')
    duration = CharField(max_length=100)
    depart_time = DateField()
    return_time = DateField()
    destination = CharField(max_length=255)
    slug = SlugField(max_length=255)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Packages.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.name)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = CharField(max_length=255)
    email = CharField(max_length=255)
    subject = CharField(max_length=255)
    message = TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = CharField(max_length=255)
    packages = models.ForeignKey(Packages, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    phone = CharField(max_length=25)
    additional_info = TextField(null=True, blank=True)

    def __str__(self):
        return self.name
