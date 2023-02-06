from django.contrib import admin
from . import models
# Register your models here.
class invtryAdmin(admin.ModelAdmin):
    list_display = ('invtry_prdctName', 'invtry_color', 'invtry_prdctBnldType','invtry_qty')
    pass

class rwMaterialsAdmin(admin.ModelAdmin):
    list_display = ('rwMaterials_name','rwMaterials_type')
    pass

admin.site.register(models.invtry,invtryAdmin)
admin.site.register(models.rwMaterials,rwMaterialsAdmin)