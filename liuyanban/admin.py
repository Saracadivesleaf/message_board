from django.contrib import admin
from liuyanban.models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
	list_display = ( 'name', )

admin.site.register(Message, MessageAdmin)