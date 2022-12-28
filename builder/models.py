from django.db import models
from decimal import Decimal

from inventory.constants import Category


class BuildStatus(models.IntegerChoices):
    DRAFT = 0
    REVIEW = 1
    FINALIZED = 2
    ARCHIVED = -1


class CustomBuild(models.Model):
    name = models.CharField(max_length=256, default="My Build")
    author = models.ForeignKey("auth.User", related_name="builds", on_delete=models.CASCADE)
    status = models.IntegerField(choices=BuildStatus.choices, default=BuildStatus.DRAFT)
    components = models.ManyToManyField("inventory.Component", related_name="builds_using")
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"

    def get_subtotal(self):
        subtotal = Decimal(0.0)
        for component in self.components.all():
            subtotal += component.price or Decimal(0.0)
        return subtotal

    def get_estimated_cost(self):
        cost = Decimal(0.0)
        for component in self.components.all():
            cost += component.cost or Decimal(0.0)
        return cost

    def is_complete(self):
        has_keyboard_base = False
        has_switches = False
        has_keycaps = False
        has_cable = False
        wireless = False
        if self.components.filter(category=Category.KEYBOARD_COMPLETE).exists():
            return True
        for kb in self.components.filter(category=Category.KEYBOARD_BAREBONES).all():
            has_keyboard_base = has_keyboard_base or True
            has_switches = has_switches or kb.tags.filter(name="includes_switches").exists()
            has_keycaps = has_keycaps or kb.tags.filter(name="includes_keycaps").exists()
            has_cable = has_cable or kb.tags.filter(name="includes_cable").exists()
            wireless = wireless or kb.tags.filter(
                models.Q(name="wireless") | models.Q(name="bluetooth")).exists()
        return has_keyboard_base and has_switches and has_keycaps and (wireless or has_cable)
