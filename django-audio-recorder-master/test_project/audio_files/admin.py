from django.contrib import admin

# Register your models here.
from .models import AudioFile,Signup

admin.site.register(AudioFile)
admin.site.register(Signup)

