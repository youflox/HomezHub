from django.contrib import admin
from .models import Requests
# Register your models here.

# admin.site.register(Requests)


class RequestsAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'date', 'status')
    readonly_fields = ['description', 'user', 'date', 'city', 'state','phone','pin','type']
    fields = (
        'type',
        'description',
        'city',
        'state',
        'pin',
        'phone',
        'status',
        'remarks',
    )

    def save_model(self, request, obj, form, change):
        obj.editor = request.user

        obj.updated = request.user

        print(obj.updated, obj.id)
        return super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(Requests, RequestsAdmin)