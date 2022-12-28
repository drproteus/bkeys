import uuid
from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator

from inventory.constants import Category


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=128, unique=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"


class Component(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256, blank=False, unique=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal(0.0))],
        default=Decimal(0.0),
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal(0.0))],
        default=Decimal(0.0),
    )
    drop_shipped = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    """If not drop-shipped, how many of this component are available"""
    url = models.CharField(max_length=1024, blank=True)
    """Link to related Amazon or other vendor URL"""
    notes = models.TextField(blank=True)
    """Internal notes about the item"""
    about = models.TextField(blank=True)
    """Component description displayed to user"""
    metadata = models.JSONField(default=dict, blank=True)
    """Extra metadata in JSON"""
    tags = models.ManyToManyField("inventory.Tag", related_name="+", blank=True)
    category = models.CharField(
        max_length=128, choices=Category.choices, null=True, blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        cat = f" ({self.category})" if self.category else ""
        return f"<{self.__class__.__name__}: {self.name}{cat}>"

    @property
    def default_image(self):
        images = self.images.all()
        if images.count() < 2:
            return images.first()
        return self.images.filter(default=True).first()

    def save(self, *args, **kwargs):
        self.metadata = self.metadata or {}
        super().save(*args, **kwargs)


class Image(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    default = models.BooleanField(default=False)
    file = models.ImageField(upload_to="images/components/")
    component = models.ForeignKey(
        "inventory.Component", related_name="images", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.name and self.file:
            self.name = self.file.name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name} ({self.file.url})>"
