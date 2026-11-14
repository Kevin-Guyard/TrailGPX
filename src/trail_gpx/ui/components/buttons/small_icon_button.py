import flet as ft
from typing import Final, Self

from ... import theme


class SmallIconButtonIcons:
    """Predefined icons for common small-button actions."""

    ADD_FOLDER: Final[ft.IconData] = ft.Icons.CREATE_NEW_FOLDER
    ADD_ROUTE: Final[ft.IconData] = ft.Icons.ROUTE
    DELETE: Final[ft.IconData] = ft.Icons.DELETE
    DOWNLOAD: Final[ft.IconData] = ft.Icons.DOWNLOAD_FOR_OFFLINE
    OPTIONS: Final[ft.IconData] = ft.Icons.MORE_VERT
    SETTINGS: Final[ft.IconData] = ft.Icons.SETTINGS
    RETURN: Final[ft.IconData] = ft.Icons.ARROW_BACK
    START_ROUTE: Final[ft.IconData] = ft.Icons.NEAR_ME


@ft.control()
class SmallIconButton(ft.IconButton):
    """A compact, circular icon button styled with the application theme."""

    def __init__(
        self: Self,
        *,
        icon: ft.IconDataOrControl,
        on_click: ft.ControlEventHandler[ft.IconButton] | None = None,
    ) -> None:
        """Initialize the button with an icon and an optional click handler.

        Parameters
        ----------
        icon : ft.IconDataOrControl
            Icon data or a Flet control displayed inside the button.
        on_click : ft.ControlEventHandler[ft.IconButton] or None, optional
            Callback invoked when the button is clicked. It may accept no
            arguments or a Flet event for the button. Defaults to None.
        """

        super().__init__(
            icon=icon,
            icon_color=theme.SMALL_ICON_BUTTON.ICON_COLOR,
            icon_size=theme.SMALL_ICON_BUTTON.ICON_SIZE,
            # Remove default padding to fit the icon in the compact themed size.
            padding=0,
            bgcolor=theme.SMALL_ICON_BUTTON.BG_COLOR,
            width=theme.SMALL_ICON_BUTTON.BUTTON_SIZE,
            height=theme.SMALL_ICON_BUTTON.BUTTON_SIZE,
            style=ft.ButtonStyle(shape=ft.CircleBorder()),
            on_click=on_click,
        )
