from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class Category(TextChoices):
    KEYBOARD_COMPLETE = "keyboard", _("Keyboard (Complete)")
    KEYBOARD_BAREBONES = "barebones", _("Keyboard (Barebones)")
    SWITCHES = "switches", _("Switches")
    KEYCAPS = "keycaps", _("Keycaps")
    CABLE = "cable", _("Cable")
    ACCESSORY = "accessory", _("Accessory")
    OTHER = "other", _("Other")
