from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.a
#admin.site.register([Test,Contact,Tag])
from django.contrib import admin
from TestModel.models import Test,Contact,Tag
 
# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age','email') #list
    inlines = [TagInline]  #inlide
    search_fields = ('name',)
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )
 
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
