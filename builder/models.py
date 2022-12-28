from django.db import models
from decimal import Decimal


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
