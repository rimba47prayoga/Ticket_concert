from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(Ticket_transaction)
admin.site.register(Cart)
admin.site.register(Transaction_info)