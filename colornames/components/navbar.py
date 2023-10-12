import reflex as rx

from ..utils import Themer, tint, shade


def navbar(themer: Themer, title: str) -> rx.Box:
    hover_l, hover_d = themer.get_color("bg")

    return rx.box(
        rx.hstack(
            rx.heading(
                title,
                font_family="Space Mono",
                color=themer.cond("bg"),
            ),
            rx.spacer(),
            rx.color_mode_button(
                rx.color_mode_icon(),
                color=themer.cond("text"),
                bg=themer.cond("bg"),
                _hover={
                    "bg": rx.color_mode_cond(shade(hover_l), tint(hover_d)),
                },
                float="right",
            ),
        ),
        width="100%",
        padding=8,
        bg=themer.cond("text"),
    )
