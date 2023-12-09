from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Company, Doc, User

admin.site.register(Company)
admin.site.register(Doc)
admin.site.register(User)