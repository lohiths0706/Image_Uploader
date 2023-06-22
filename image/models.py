from inspect import modulesbyfile
from django.db import models
import csv
from django.db import models
# from django.db.models import Model

from django.conf import settings
from django.conf.urls.static import static


class Image(models.Model):
 photo =models.ImageField(upload_to= "myimage")
 data=models.DateTimeField(auto_now_add=True)
