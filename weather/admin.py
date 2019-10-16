from django.contrib import admin
from .models import Location, User
from django.contrib import admin
from .forms import SubscribeForm

# Register your models here.
admin.site.register(Location)

class UserAdmin(admin.ModelAdmin):
    form = SubscribeForm

admin.site.register(User, UserAdmin)