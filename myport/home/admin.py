from django.contrib import admin
from .models import Contact , Myprojects
from .models import files
# Register your models here.
admin.site.register(Contact)
admin.site.register(Myprojects)
admin.site.register(files)