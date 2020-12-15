from django.contrib import admin
from collection.models import Books

class ThingAdmin(admin.ModelAdmin):
    model = Books
    list_display = ('title', 'author','description',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Books, ThingAdmin)

