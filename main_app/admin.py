from django.contrib import admin

from django.contrib import admin
from .models import Tiger, Feeding, Toy


# Register your models here.
admin.site.register(Tiger)
admin.site.register(Feeding)
admin.site.register(Toy)