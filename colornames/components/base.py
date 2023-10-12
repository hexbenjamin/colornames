import reflex as rx

from ..utils import Themer


def base(thm: Themer) -> rx.Box:
    return rx.box(
        width="100%",
        height="90vh",
        bg=thm.cond("bg"),
        padding=8,
    )
