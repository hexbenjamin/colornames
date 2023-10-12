import reflex as rx

from ..components import navbar, color_picker
from ..utils import State, Themer


def layout(themer: Themer):
    return rx.box(
        rx.center(
            rx.vstack(
                rx.box(
                    height="128px",
                    width="100%",
                    bg=State.color,
                    border_radius="12px",
                ),
                rx.hstack(
                    color_picker(on_change=State.set_color),
                    rx.vstack(
                        rx.input(
                            value=State.color.upper(),
                            on_change=State.set_color,
                            margin=8,
                            padding=8,
                            font_family="Space Mono",
                            font_size=24,
                            color=themer.cond("text"),
                            border_radius="12px",
                            width="42%",
                        ),
                        rx.button_group(
                            rx.button(
                                "RANDOMIZE",
                                variant="outline",
                                on_click=State.randomize_color,
                                font_family="Space Mono",
                            ),
                            rx.button(
                                "GET NAME",
                                on_click=State.update_name,
                                font_family="Space Mono",
                            ),
                        ),
                    ),
                ),
                rx.spacer(),
                rx.center(
                    rx.box(
                        rx.heading(
                            State.name,
                            font_family="Space Mono",
                            font_weight="800",
                            font_size="48px",
                        ),
                        padding=8,
                        # border="2px solid " + State.color,
                        # border_radius="12px",
                    ),
                    width="100%",
                ),
                spacing="16px",
                justify_content="space-between",
                width="66%",
            ),
        ),
        padding=12,
        width="100%",
        height="90vh",
        bg=themer.cond("bg"),
    )


def index(themer: Themer) -> rx.Component:
    """The app frontend."""

    return rx.vstack(
        navbar(themer, "colornames!"),
        layout(themer),
        spacing="0px",
    )
