import flet as ft
from typing import Final


class TEXT_SIZE:

    NORMAL: Final[float | int] = 16
    SUB: Final[float | int] = 12
    ERROR: Final[float | int] = 12
    IMPORTANT: Final[float | int] = 20

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

class GPX_FILE_PICKER:

    BORDER_RADIUS: Final[float | int] = 8
    BORDER_WIDTH: Final[float | int] = 1

    PADDING_LEFT: Final[float | int] = 12
    PADDING_TOP: Final[float | int] = 20
    PADDING_RIGHT: Final[float | int] = 12
    PADDING_BOTTOM: Final[float | int] = 12

    ICON_SIZE = 30

    BG_COLOR: Final[str | ft.Colors] = "#FFFFFF"

class SMALL_ICON_BUTTON:

    ICON_COLOR: Final[str | ft.Colors] = "#000000"
    ICON_SIZE: Final[float | int] = 25

    BUTTON_SIZE: Final[float | int] = ICON_SIZE * 1.5

    BG_COLOR: Final[str | ft.Colors] = ft.Colors.TRANSPARENT

class MEDIUM_BUTTON:

    WIDTH: Final[float | int] = 150
    HEIGHT: Final[float | int] = 40
    RADIUS: Final[float | int] = 30

    TEXT_COLOR_ENABLED: Final[str | ft.Colors] = "#FFFFFF"
    TEXT_COLOR_DISABLED: Final[str | ft.Colors] = "#757575"

    BORDER_WIDTH: Final[float | int] = 2
    BORDER_COLOR_ENABLED: Final[str | ft.Colors] = "#000000"
    BORDER_COLOR_DISABLED: Final[str | ft.Colors] = "#D0D0D0"

    ELEVATION_ENABLED: Final[float | int] = 8
    ELEVATION_DISABLED: Final[float | int] = 4

    BG_ENABLED: Final[str | ft.Colors] = "#000000"
    BG_DISABLED: Final[str | ft.Colors] = "#E0E0E0"

class GPX_INFOS_DISPLAY:

    ICON_SIZE: Final[float | int] = 24
    ICON_COLOR: Final[str | ft.Colors] = "#000000"

    SPACING_AFTER_TITLE: Final[float | int] = 4
    SPACING_BETWEEN_ICON_AND_METRIC: Final[float | int] = 4
    SPACING_BETWEEN_METRIC_BLOCS: Final[float | int] = 10

class FOLDER_AND_ROUTE_CARD:

    BORDER_WIDTH: Final[float | int] = 1
    BORDER_RADIUS: Final[float | int] = 12

    PADDING_HORIZONTAL: Final[float | int] = 16
    PADDING_VERTICAL: Final[float | int] = 12

    MAIN_ICON_SIZE: Final[float | int] = 30
    MAIN_ICON_COLOR: Final[str | ft.Colors] = "#000000"

    METRIC_ICON_SIZE: Final[float | int] = 16
    METRIC_ICON_COLOR: Final[str | ft.Colors] = "#000000"

    SPACING_BETWEEN_ICON_AND_TEXT: Final[float | int] = 16
    SPACING_BETWEEN_TWO_LINES: Final[float | int] = 0

    SPACING_BETWEEN_ICON_AND_METRIC: Final[float | int] = 2
    SPACING_BETWEEN_METRICS: Final[float | int] = 4

    BG_COLOR: Final[str | ft.Colors] = "#FFFFFF"

class GPX_DETAIL_INFOS_DISPLAY:

    ICON_SIZE: Final[float | int] = 20
    ICON_COLOR: Final[str | ft.Colors] = "#000000"

    SPACING_AFTER_TITLE: Final[float | int] = 16
    SPACING_BETWEEN_TWO_LINES: Final[float | int] = 10
    SPACING_BETWEEN_ICON_AND_TEXT: Final[float | int] = 8