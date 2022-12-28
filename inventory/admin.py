from django.contrib import admin
from django.utils.html import format_html
from inventory.models import (
    Tag, Component, Image
)


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = (
        "name", "preview",
        "cost", "price",
        "drop_shipped", "stock",
        "description", "_tags",)
    inlines = [ImageInline]

    def _tags(self, obj):
        return ", ".join(obj.tags.values_list("name", flat=True))

    def preview(self, obj):
        img = obj.default_image
        if not img:
            return ""
        return format_html(f"<img width=\"100px\" src=\"{img.file.url}\">")
    preview.allow_tags = True

    def description(self, obj):
        parts = []
        if obj.about:
            parts.append(f"<b>About:</b> {obj.about}")
        if obj.notes:
            parts.append(f"<b>Notes:</b> {obj.about}")
        if obj.metadata:
            for key, value in obj.metadata.items():
                parts.append(f"<b>{key}:</b> {value}")
        return format_html("\n".join(parts))
    description.allow_tags = True


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "hidden",)
