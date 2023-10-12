import json

import reflex as rx

from .pages import index
from .utils import State, Themer


with open("assets/theme.json", "r") as f:
    thm = Themer.from_dict(json.load(f))

app = rx.App(
    state=State,
)
app.add_page(index(thm), route="/")
app.compile()
