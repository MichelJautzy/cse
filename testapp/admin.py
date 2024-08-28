from django.contrib import admin
from .models import ModelTest, ModelToto 

# Register your models here.
admin.site.register(ModelTest)
admin.site.register(ModelToto)