from django.contrib import admin


from boat.models import Owner, Boat, BoatHistory


@admin.register(Owner)
class Owner(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Boat)
class Boat(admin.ModelAdmin):
    list_display = ('name', 'year', 'owner', )
    list_filter = ('year', 'owner', )


@admin.register(BoatHistory)
class BoatHistory(admin.ModelAdmin):
    list_display = ('boat', 'start_year', 'stop_year', 'owner', )
    list_filter = ('boat', 'owner', )


