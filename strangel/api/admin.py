from django.contrib import admin
from .models import User, Safepoints

# Register your models here.
admin.site.register(User)
admin.site.register(Safepoints)