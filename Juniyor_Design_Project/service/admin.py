from django.contrib import admin

from .models import Item1
from .models import Academic
from .models import Financial
from .models import User1


# Register your models here.

admin.site.register(Item1)
admin.site.register(Academic)
admin.site.register(Financial)
admin.site.register(User1)

