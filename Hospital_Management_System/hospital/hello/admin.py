from django.contrib import admin
from .models import User1
from .models import Bed
from .models import Test
from .models import Nurse
from .models import Medicine
from .models import Patient
from .models import Doctor
from .models import BloodDonate
from .models import Appointment
from .models import OrganDonate
from .models import Story


# Register your models here.

admin.site.register(Bed)
admin.site.register(Appointment)
admin.site.register(Test)
admin.site.register(User1)
admin.site.register(Medicine)
admin.site.register(BloodDonate)
admin.site.register(OrganDonate)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Story)
admin.site.register(Nurse)
