import flet as ft
from typing import Final


class TEXT_SIZE:

    NORMAL: Final[float | int] = 16
    ERROR: Final[float | int] = 12

class TEXT_COLOR:

    NORMAL: Final[str | ft.Colors] = "#000000"
    ERROR: Final[str | ft.Colors] = "#F44336"
    HINT: Final[str | ft.Colors] = "#CFCFCF"
    LIGHT: Final[str | ft.Colors] = "#8F8F8F"

class BORDER_COLOR:

    NORMAL: Final[str | ft.Colors] = "#000000"
    ERROR: Final[str | ft.Colors] = "#F44336"
    LIGHT: Final[str | ft.Colors] = "#8F8F8F"

class TEXT_FIELD:

    BORDER_RADIUS: Final[float | int] = 8

    BORDER_WIDTH_NOT_FOCUSED: Final[float | int] = 1
    BORDER_WIDTH_FOCUSED: Final[float | int] = 2

    PADDING_LEFT: Final[float | int] = 12
    PADDING_TOP: Final[float | int] = 20
    PADDING_RIGHT: Final[float | int] = 12
    PADDING_BOTTOM: Final[float | int] = 12

    BG_COLOR: Final[str | ft.Colors] = "#FFFFFF"