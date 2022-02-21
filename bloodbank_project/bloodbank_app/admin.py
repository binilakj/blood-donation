from django.contrib import admin
from . models import Blood_Bank,Districts,Centers
# Register your models here.
admin.site.register(Blood_Bank)

class DistrictAdmins(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Districts,DistrictAdmins)


class CentersAdmins(admin.ModelAdmin):
    list_display= ['name','category','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Centers,CentersAdmins)
