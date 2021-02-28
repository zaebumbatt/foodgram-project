from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'first_name')


admin.site.unregister(Group)
