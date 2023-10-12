import reflex as rx

from .colors import validate_hex


class Themer:
    def __init__(self):
        self.colors = {}

    @classmethod
    def from_dict(cls, colors: dict):
        themer = cls()
        for name, colors in colors.items():
            themer.add_color(name, colors["light"], colors["dark"])
        return themer

    def add_color(self, name: str, light: str, dark: str) -> None:
        validate_hex(light)
        validate_hex(dark)
        self.colors[name] = {
            "light": light.lower(),
            "dark": dark.lower(),
        }

    def remove_color(self, name: str) -> None:
        self.colors.pop(name)

    def get_color(self, name: str) -> tuple:
        if not name in self.colors:
            raise ValueError(f"'{name}' is not a registered color name.")

        return self.colors[name]["light"], self.colors[name]["dark"]

    def cond(self, name: str):
        if not name in self.colors:
            raise ValueError(f"'{name}' is not a registered color name.")

        c = self.colors[name]

        return rx.color_mode_cond(c["light"], c["dark"])
