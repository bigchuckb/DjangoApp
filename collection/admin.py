from django.contrib import admin
from collection.models import Books, Rating, Shtetl

class ThingAdmin(admin.ModelAdmin):
    model = Books
    list_display = ('title', 'author','description','owner')
    prepopulated_fields = {'slug': ('title',)}

class RatingAdmin(admin.ModelAdmin):
    model = Rating
    list_display = ('rating','user','book')

class ShtetlAdmin(admin.ModelAdmin):
    model = Shtetl
    list_display = ('game_played','winner')

admin.site.register(Books, ThingAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Shtetl, ShtetlAdmin)


