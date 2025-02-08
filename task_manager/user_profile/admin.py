from django.contrib import admin

from .models import Profile, SocialLinks


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'owner', 'bio', 'privacy'
    )
    search_fields = ('owner', 'bio')
    empty_value_display = 'NULL'


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = (
        'profile',
    )
    search_fields = ('profile',)
    empty_value_display = 'NULL'


admin.site.register(Profile, ProfileAdmin)
admin.site.register(SocialLinks, SocialLinksAdmin)
