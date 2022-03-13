from django.contrib import admin
from . models import user
from . import models
from django.contrib import messages


@admin.action(description='approve new user')
def make_published(modeladmin, request, queryset):
    queryset.update(status='a')

class userAdmin(admin.ModelAdmin):
    list_display = ['username','email','status']
    ordering = ['username']
    actions = [make_published]

    
admin.site.register(user,userAdmin)
  
class blogadminarea(admin.AdminSite):
    site_header = 'Blog Database'

class testadminpermissions(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return True

    def has_edit_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):

        if obj != None and request.POST.get('action') =='delete_selected':
            messages.add_message(request, messages.ERROR,(
                "I really hope you are sure about this!"
            ))

        if request.user.groups.filter(name='editors').exists():
            return True

        return obj
    
    def has_view_permission(self, request, obj=None):
        return True


blog_site = blogadminarea(name='BlogAdmin')

blog_site.register(models.post, testadminpermissions)
blog_site.register(models.user)







