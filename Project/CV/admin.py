from django.contrib import admin
from .models import *
# Register your models here.

class portfolioImageInline(admin.StackedInline):
    model = portfolioImage

class portfolioadmin(admin.ModelAdmin):
    inlines = [portfolioImageInline]

admin.site.register(Portfolio, portfolioadmin)
admin.site.register(Mainsection)
admin.site.register(subsection)