from django.contrib import admin
from .models import VoteTitle, Vote

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"


class ChoiceInline(admin.TabularInline):
    model = Vote
    extra = 3

class VoteTitleAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']}),
                  ('Date Information', {'fields': ['date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(VoteTitle, VoteTitleAdmin)
admin.site.register(Vote)

