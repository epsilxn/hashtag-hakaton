from django.contrib import admin
from .models import ParentUser, Child


admin.site.register(ParentUser)
admin.site.register(Child)