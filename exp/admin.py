from django.contrib import admin
# from .models import UserModels,LocalService,RemoteService
# # Register your models here.
# admin.site.register(UserModels)
# admin.site.register(LocalService)
# admin.site.register(RemoteService)
# Register your models here.
from .models import cab,Hotels,lodge,places
admin.site.register(cab)
admin.site.register(lodge)
admin.site.register(Hotels)
admin.site.register(places)