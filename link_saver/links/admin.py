from django.contrib import admin
from .models import link
# Register your models here.
class LinkAdmin(admin.ModelAdmin):
	list_display = ["links", "date"]
	list_filter = ["date"]
	class Meta:
		model = link
admin.site.register(link, LinkAdmin )