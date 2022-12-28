from django.contrib import admin
from builder.models import CustomBuild


@admin.register(CustomBuild)
class CustomBuildAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "_components", "subtotal", "estimated_cost",)

    def subtotal(self, obj):
        return obj.get_subtotal()

    def estimated_cost(self, obj):
        return obj.get_estimated_cost()

    def _components(self, obj):
        parts = []
        for component in obj.components.all():
            part_str = component.name
            if component.category is not None:
                part_str += f" ({component.category})"
            parts.append(part_str)
        return "<br>".join(parts)
    _components.allow_tags = True
