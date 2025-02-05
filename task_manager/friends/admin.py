from django.contrib import admin

from .models import Friendship, FriendshipRequest


class FriendshipAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'user', 'friend'

    )
    search_fields = ('user__username', 'friend__username')


class FriendshipRequestAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'from_user', 'to_user'
    )
    search_fields = ('from_user__username', 'to_user__username')


admin.site.register(Friendship, FriendshipAdmin)
admin.site.register(FriendshipRequest, FriendshipRequestAdmin)
