from django.contrib import admin
from booking.models import Service, Duration, Extra, Mani, Pedi

# Register your models here.
admin.site.register(Service)
admin.site.register(Duration)
admin.site.register(Extra)
admin.site.register(Mani)
admin.site.register(Pedi)