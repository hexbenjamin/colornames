from random import randint

import httpx
import reflex as rx


class State(rx.State):
    color: str = "#000000"
    name: str = "Black"

    def randomize_color(self) -> None:
        """Randomize the color."""
        r, g, b = [randint(0, 255) for _ in range(3)]
        self.color = f"#{r:02x}{g:02x}{b:02x}"

    def update_name(self) -> None:
        r = httpx.get(
            "https://api.color.pizza/v1/",
            params={"values": self.color.strip("#")},
        )
        self.name = r.json()["colors"][0]["name"]
