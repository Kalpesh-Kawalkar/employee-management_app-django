from django.contrib import admin
from.models import Emp,Testimonial
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ('name','working','emp_id','phone','address')
    list_editable = ('working','emp_id','address')
    search_fields = ('name','phone')
admin.site.register(Emp,EmpAdmin)