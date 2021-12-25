from friendships.models import Friendship
from django.contrib import admin

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user', 'created_at')
    date_hierarchy = 'created_at'