from django.contrib import admin



from .models import Source, Definition, DefinitionSource


class DefinitionSourceInline(admin.TabularInline):
    model = DefinitionSource


class DefinitionAdmin(admin.ModelAdmin):
    search_fields = ('name_ru', 'name_en', 'name_de')
    inlines = [DefinitionSourceInline,]


admin.site.register(Definition, DefinitionAdmin)
admin.site.register(Source)
