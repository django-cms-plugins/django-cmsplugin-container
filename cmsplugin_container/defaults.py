#-*- coding: utf-8 -*-
from django.conf import settings


if hasattr(settings, 'CMS_CONTAINER_WIDTH_CHOICES'):
    CONTAINER_WIDTH_CHOICES = settings.CMS_CONTAINER_WIDTH_CHOICES
else:
    CONTAINER_WIDTH_CHOICES = (
        ('10%', '10%'),
        ('20%', '20%'),
        ('25%', '25%'),
        ('30%', '30%'),
        ('33.33%', '33%'),
        ('40%', '40%'),
        ('50%', '50%'),
        ('66.66%', '66%'),
        ('60%', '60%'),
        ('70%', '70%'),
        ('75%', '75%'),
        ('80%', '80%'),
        ('90%', '90%'),
        ('100%', '100%'),
    )

if hasattr(settings, 'CMS_CONTAINER_CLASS_CHOICES'):
    CONTAINER_CLASS_CHOICES = settings.CMS_CONTAINER_CLASS_CHOICES
else:
    CONTAINER_CLASS_CHOICES = (
        ('grid_12', 'Grid 12'),
        ('grid_16', 'Grid 16'),
    )
