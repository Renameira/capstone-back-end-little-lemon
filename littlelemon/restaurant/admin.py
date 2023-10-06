from django.contrib import admin
from .models import Booking, MenuItens

admin.site.register([Booking, MenuItens])
