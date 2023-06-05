from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'city',
                    'gender', 'birthday', 'language', 'number_card']
    search_fields = ['first_name', 'last_name']
    list_filter = ['gender', 'language', 'city']
    # list_editable = []
    fields = ['first_name', 'last_name', 'email', 'phone', 'city',
              'gender', 'birthday', 'language', 'number_card']
    # readonly_fields = ['create_time', 'update_time']


admin.site.register(CustomUser, CustomUserAdmin)
