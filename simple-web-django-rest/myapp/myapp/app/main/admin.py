
from django.contrib import admin

from myapp.app.main.models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Work)
admin.site.register(Contracts)
