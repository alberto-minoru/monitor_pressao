from django.contrib import admin
from .models import Pressao


class PressaoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'data', 'sis', 'dia')


admin.site.register(Pressao, PressaoAdmin)
