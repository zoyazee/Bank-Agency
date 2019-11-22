from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
	list_display = ("agent_name","location","daily_transaction","internal_branding_photo","external_branding_photo","tariffs_display_photo")
	search_fields = ("agent_name","location",)


admin.site.register(Agent,AgentAdmin)

# Register your models here.
