from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

#unregister Groups
admin.site.unregister(Group)


# Mix profile info into User info

class ProfileInLine(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Just desplay username fields on admin page
    fields = ['username']
    inlines = [ProfileInLine]


# Unregister Initial User
admin.site.unregister(User)

# Register User and Profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)



