import re

from colour import Color

import reflex as rx


def validate_hex(hex_color: str) -> None:
    if not re.match(r"^#(?:[0-9a-fA-F]{3}){1,2}$", hex_color):
        raise ValueError(f"'{hex_color}' is not a valid hex color code.")


def tint(color: str):
    validate_hex(color)
    c = Color(color)
    c.luminance += 0.17
    return c.hex_l


def shade(color: str):
    validate_hex(color)
    c = Color(color)
    c.luminance -= 0.13
    return c.hex_l
