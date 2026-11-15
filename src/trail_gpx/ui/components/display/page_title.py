import flet as ft
from typing import Self

from ... import theme


@ft.control()
class PageTitle(ft.Text):
    """Display a centered page title using the application theme."""

    def __init__(self: Self, title: str) -> None:
        """Initialize the page title.

        Parameters
        ----------
        title : str
            Text to display as the page title.
        """

        super().__init__(
            value=title,
            # Fill the available width so the title is centered in its parent.
            expand=True,
            size=theme.TEXT_SIZE.TITLE,
            color=theme.TEXT_COLOR.NORMAL,
            weight=ft.FontWeight.BOLD
        )
