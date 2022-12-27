import uuid
from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator


class BaseComponent(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256, blank=False, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal(0.0))], default=Decimal(0.0))
    """Component price in USD cents"""
    drop_shipped = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    url = models.CharField(max_length=1024, blank=True)
    notes = models.TextField(blank=True)
    """Internal notes about the item"""
    about = models.TextField(blank=True)
    """Component description displayed to user"""
    metadata = models.JSONField(default=dict, blank=True)
    """Extra metadata in JSON"""
    album = models.ForeignKey(
        "inventory.ImageAlbum", related_name="+",
        on_delete=models.CASCADE, null=True, blank=True)


class Component(BaseComponent):
    pass


FORM_FACTORS = [
    ("60", "60%"),
    ("65", "65%"),
    ("75", "75%"),
    ("80", "80%"),
    ("95", "95%"),
    ("100", "100%"),
    ("numpad", "numpad"),
    ("macro", "macro"),
    ("custom", "custom"),
]
INPUT_OPTIONS = [
    ("micro", "Micro USB"),
    ("mini", "Mini USB"),
    ("type-c", "USB-C"),
]
OUTPUT_OPTIONS = [
    ("type-a", "USB-A"),
    ("type-c", "USB-C"),
]
SWITCH_TYPES = [
    ("mechanical_linear", "Linear"),
    ("mechanical_tactile", "Tactile"),
    ("mechanical_clicky", "Clicky"),
    ("optical", "Optical"),
    ("hybrid", "Hybrid"),
    ("topre", "Topre"),
    ("other", "Other"),
]
WIRELESS_MODES = [
    ("bluetooth", "Bluetooth"),
    ("2.4ghz", "2.4GHz"),
    ("combo", "Bluetooth and 2.4GHz"),
]
KEYCAP_MATERIALS = [
    ("abs", "ABS"),
    ("pbt", "PBT"),
    ("wood", "Wood"),
    ("other", "Other")
]


class Keyboard(BaseComponent):
    form_factor = models.CharField(max_length=128, choices=FORM_FACTORS, default="custom")
    key_count = models.PositiveIntegerField(default=0)

    hot_swappable = models.BooleanField(default=False)

    switches = models.CharField(
        max_length=128, choices=SWITCH_TYPES, null=True, blank=True)
    keycaps = models.CharField(
        max_length=128, choices=KEYCAP_MATERIALS, null=True, blank=True)
    wireless_mode = models.CharField(
        max_length=128, choices=WIRELESS_MODES, null=True, blank=True)
    input = models.CharField(
        max_length=128, choices=INPUT_OPTIONS, default="type-c", null=True, blank=True)
    output = models.CharField(max_length=128, choices=OUTPUT_OPTIONS, null=True, blank=True)


class SwitchSet(BaseComponent):
    switch_type = models.CharField(
        max_length=128, choices=SWITCH_TYPES, blank=True, default="other")
    count = models.PositiveIntegerField(default=0)


class KeycapSet(BaseComponent):
    material = models.CharField(
        max_length=128, choices=KEYCAP_MATERIALS, blank=True, default="other")
    count = models.PositiveIntegerField(default=0)


class Cable(BaseComponent):
    input = models.CharField(max_length=128, choices=INPUT_OPTIONS, default="micro")
    output = models.CharField(max_length=128, choices=OUTPUT_OPTIONS, default="type-a")
    length_cm = models.DecimalField(
        max_digits=4, decimal_places=2,
        validators=[MinValueValidator(Decimal(0.0))], default=Decimal(0.0))


# IMAGES
def get_upload_path(instance, filename):
    model = instance.album.__class__._meta
    name = model.verbose_name_plural.replace(" ", "_")
    return f"{name}/images/{filename}"


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()


class Image(models.Model):
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    album = models.ForeignKey(
        "inventory.ImageAlbum", related_name="images", on_delete=models.CASCADE)
