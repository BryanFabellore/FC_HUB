from django.contrib import admin
from . import models
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('usr_username','fName','lName')
    pass

admin.site.register(models.user_acc,UsersAdmin)