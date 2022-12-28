from django.contrib import admin
from django.utils.html import format_html
from inventory.models import (
    Component,
    Keyboard,
    Cable,
    KeycapSet,
    SwitchSet,
    ComponentImage,
    KeyboardImage,
    CableImage,
    KeycapSetImage,
    SwitchSetImage,
)


class ComponentImageInline(admin.StackedInline):
    model = ComponentImage
    extra = 0


class KeyboardImageInline(admin.StackedInline):
    model = KeyboardImage
    extra = 0


class CableImageInline(admin.StackedInline):
    model = CableImage
    extra = 0


class KeycapSetImageInline(admin.StackedInline):
    model = KeycapSetImage
    extra = 0


class SwitchSetImageInline(admin.StackedInline):
    model = SwitchSetImage
    extra = 0


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "admin_image")
    inlines = [ComponentImageInline]

    def admin_image(self, obj):
        img = obj.default_image
        if not img:
            return ""
        return format_html(f"<img width=\"100px\" src=\"{img.image.url}\">")
    admin_image.allow_tags = True


@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    inlines = [KeyboardImageInline]


@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    inlines = [CableImageInline]


@admin.register(KeycapSet)
class KeycapSetAdmin(admin.ModelAdmin):
    inlines = [KeycapSetImageInline]


@admin.register(SwitchSet)
class SwitchSetAdmin(admin.ModelAdmin):
    inlines = [SwitchSetImageInline]
