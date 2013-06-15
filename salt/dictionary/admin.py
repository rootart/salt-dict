from django.contrib import admin



from .models import Source, Definition, DefinitionSource


class DefinitionSourceInline(admin.TabularInline):
    model = DefinitionSource


class DefinitionAdmin(admin.ModelAdmin):
    fields_search = ('name_ru',)
    inlines = [DefinitionSourceInline,]


admin.site.register(Definition, DefinitionAdmin)
admin.site.register(Source)
