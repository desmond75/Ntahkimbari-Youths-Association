from django.contrib import admin
from .models import Member, Community_work, Post, Event
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Member, UserAdmin)
admin.site.register(Community_work)
class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'description', 'tag', 'photo', 'project_completed']
	list_display = ('title','id', 'post_date', 'tag', 'project_completed')

admin.site.register(Post, PostAdmin)

class EventAdmin(admin.ModelAdmin):
	fields = ['title', 'description', 'event_date', 'event_time']
	list_display = ('title','event_date', 'event_time','post_date')


admin.site.register(Event, EventAdmin)

