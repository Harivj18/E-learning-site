from django.contrib import admin
from .models import page,comment
# Register your models here.
admin.site.site_header='Hari Database'

class pageAdmin(admin.ModelAdmin):
    list_filter=['Created_on']
    list_display=('Title','Created_on')

class commentAdmin(admin.ModelAdmin):
    list_filter=['Created_on']
    list_display=['name','post','Created_on']
   


admin.site.register(page,pageAdmin)
admin.site.register(comment,commentAdmin)


