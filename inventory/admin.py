from django.contrib import admin
from inventory.models import Component, Keyboard, Cable, KeycapSet, SwitchSet


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    pass


@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    pass


@admin.register(KeycapSet)
class KeycapSetAdmin(admin.ModelAdmin):
    pass


@admin.register(SwitchSet)
class SwitcheSetAdmin(admin.ModelAdmin):
    pass
