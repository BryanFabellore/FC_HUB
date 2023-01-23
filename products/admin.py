from django.contrib import admin
from . import models
# Register your models here.
class invtryAdmin(admin.ModelAdmin):
    list_display = ('invtry_prdctName','invtry_prdctBnldType','invtry_qty')
    pass

admin.site.register(models.invtry,invtryAdmin)