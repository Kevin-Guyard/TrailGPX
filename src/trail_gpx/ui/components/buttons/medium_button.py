from enum import Enum
import flet as ft
from typing import Self

from ... import theme


class MediumButtonConfig(Enum):
    """Predefined configurations for medium buttons.

    Attributes
    ----------
    icon : ft.IconData
        Icon displayed for the configuration.
    content : str
        Text displayed for the configuration.
    """

    _value_: tuple[ft.IconData, str]

    # Enum passes each tuple's items as separate constructor arguments.
    VALIDATE = (ft.Icons.CHECK, "Validate")
    SAVE = (ft.Icons.SAVE, "Save")

    def __init__(self: Self, icon: ft.IconData, content: str) -> None:
        """Initialize the icon and text of a button configuration.

        Parameters
        ----------
        icon : ft.IconData
            Icon displayed on the button.
        content : str
            Text displayed on the button.
        """
        self.icon: ft.IconData = icon
        self.content: str = content


@ft.control
class MediumButton(ft.Button):
    """A medium-sized action button styled with the application theme."""

    def __init__(
        self: Self,
        *,
        config: MediumButtonConfig,
        disabled: bool = True,
        on_click: ft.ControlEventHandler[ft.Button] | None = None,
    ) -> None:
        """Initialize the button with a predefined configuration.

        Parameters
        ----------
        config : MediumButtonConfig
            Configuration providing the button's icon and label.
        disabled : bool, optional
            Whether the button is disabled. Defaults to True.
        on_click : ft.ControlEventHandler[ft.Button] or None, optional
            Callback invoked when the button is clicked. It may accept no
            arguments or a Flet event for the button. Defaults to None.
        """
        super().__init__(
            icon=config.icon,
            content=config.content,
            disabled=disabled,
            width=theme.MEDIUM_BUTTON.WIDTH,
            height=theme.MEDIUM_BUTTON.HEIGHT,
            elevation={
                ft.ControlState.DEFAULT: theme.MEDIUM_BUTTON.ELEVATION_ENABLED,
                ft.ControlState.DISABLED: theme.MEDIUM_BUTTON.ELEVATION_DISABLED,
            },
            style=ft.ButtonStyle(
                bgcolor={
                    ft.ControlState.DEFAULT: theme.MEDIUM_BUTTON.BG_ENABLED,
                    ft.ControlState.DISABLED: theme.MEDIUM_BUTTON.BG_DISABLED,
                },
                color={
                    ft.ControlState.DEFAULT: theme.MEDIUM_BUTTON.TEXT_COLOR_ENABLED,
                    ft.ControlState.DISABLED: theme.MEDIUM_BUTTON.TEXT_COLOR_DISABLED,
                },
                text_style=ft.TextStyle(
                    size=theme.TEXT_SIZE.NORMAL,
                    weight=ft.FontWeight.BOLD,
                ),
                shape=ft.RoundedRectangleBorder(radius=theme.MEDIUM_BUTTON.RADIUS),
                side={
                    ft.ControlState.DEFAULT: ft.BorderSide(
                        width=theme.MEDIUM_BUTTON.BORDER_WIDTH,
                        color=theme.MEDIUM_BUTTON.BORDER_COLOR_ENABLED,
                    ),
                    ft.ControlState.DISABLED: ft.BorderSide(
                        width=theme.MEDIUM_BUTTON.BORDER_WIDTH,
                        color=theme.MEDIUM_BUTTON.BORDER_COLOR_DISABLED,
                    ),
                },
            ),
            on_click=on_click,
        )
