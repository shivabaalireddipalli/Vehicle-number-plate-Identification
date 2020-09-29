from django.contrib import admin
# Register your models here.
from . import models
from .models import crimefill
from .models import Databse
from .models import allvehicle
from .models import UpdateCrime

admin.site.register(crimefill)
admin.site.register(allvehicle)
admin.site.register(Databse)
admin.site.register(UpdateCrime)