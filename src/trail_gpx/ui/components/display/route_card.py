import flet as ft
from typing import Self

from ... import theme
from ..buttons import SmallIconButton, SmallIconButtonIcons


@ft.control()
class RouteCard(ft.Container):
    """Display a route's name, distance, elevation changes, and options button."""

    def __init__(
        self: Self,
        *,
        route_name: str,
        distance_km: float,
        elevation_gain_m: int,
        elevation_loss_m: int,
        on_click_options: ft.ControlEventHandler[ft.IconButton] | None = None,
        on_click_card: ft.ControlEventHandler[ft.Container] | None = None,
    ) -> None:
        """Initialize the route card and its optional click handlers.

        Parameters
        ----------
        route_name : str
            Route name displayed on the first line, truncated if necessary.
        distance_km : float
            Route distance in kilometers. Values below 100 are displayed with
            one decimal place; other values are rounded to a whole kilometer.
        elevation_gain_m : int
            Total elevation gain displayed in meters.
        elevation_loss_m : int
            Total elevation loss displayed in meters.
        on_click_options : ft.ControlEventHandler[ft.IconButton] or None, optional
            Callback invoked when the options button is clicked. Defaults to None.
        on_click_card : ft.ControlEventHandler[ft.Container] or None, optional
            Callback invoked when the card is clicked. Defaults to None.
        """

        # Keep a reference to update the name without rebuilding the card.
        self._route_name_text: ft.Text = ft.Text(
            color=theme.TEXT_COLOR.NORMAL,
            size=theme.TEXT_SIZE.NORMAL,
            weight=ft.FontWeight.BOLD,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
        )

        metric_row: ft.Row = ft.Row(
            spacing=theme.FOLDER_AND_ROUTE_CARD.SPACING_BETWEEN_METRICS,
            controls=[
                self._construct_metric_row(
                    icon=ft.Icons.STRAIGHTEN,
                    text=(
                        f"{distance_km:.1f} km"
                        if distance_km < 100.0
                        else f"{distance_km:.0f} km"
                    ),
                ),
                self._construct_metric_row(
                    icon=ft.Icons.TRENDING_UP,
                    text=f"{elevation_gain_m:d} m",
                ),
                self._construct_metric_row(
                    icon=ft.Icons.TRENDING_DOWN,
                    text=f"{elevation_loss_m:d} m",
                ),
            ],
        )

        labels: ft.Column = ft.Column(
            expand=True,
            spacing=theme.FOLDER_AND_ROUTE_CARD.SPACING_BETWEEN_TWO_LINES,
            controls=[
                self._route_name_text,
                metric_row,
            ],
        )

        route_content: ft.Container = ft.Container(
            expand=True,
            content=ft.Row(
                spacing=theme.FOLDER_AND_ROUTE_CARD.SPACING_BETWEEN_ICON_AND_TEXT,
                controls=[
                    ft.Icon(
                        icon=ft.Icons.ROUTE,
                        size=theme.FOLDER_AND_ROUTE_CARD.MAIN_ICON_SIZE,
                        color=theme.FOLDER_AND_ROUTE_CARD.MAIN_ICON_COLOR,
                    ),
                    labels,
                ],
            ),
        )

        options_button: SmallIconButton = SmallIconButton(
            icon=SmallIconButtonIcons.OPTIONS,
            on_click=on_click_options,
        )

        super().__init__(
            on_click=on_click_card,
            border=ft.Border.all(
                width=theme.FOLDER_AND_ROUTE_CARD.BORDER_WIDTH,
                color=theme.BORDER_COLOR.NORMAL,
            ),
            border_radius=theme.FOLDER_AND_ROUTE_CARD.BORDER_RADIUS,
            padding=ft.Padding.symmetric(
                horizontal=theme.FOLDER_AND_ROUTE_CARD.PADDING_HORIZONTAL,
                vertical=theme.FOLDER_AND_ROUTE_CARD.PADDING_VERTICAL,
            ),
            bgcolor=theme.FOLDER_AND_ROUTE_CARD.BG_COLOR,
            content=ft.Row(controls=[route_content, options_button]),
        )

        # The control is not mounted during construction, so skip the page update.
        self.set_infos(
            route_name=route_name,
            refreshing=False,
        )

    @staticmethod
    def _construct_metric_row(icon: ft.IconData, text: str) -> ft.Row:
        """Build a row displaying a metric icon and its formatted value.

        Parameters
        ----------
        icon : ft.IconData
            Icon identifying the metric.
        text : str
            Formatted metric value, including its unit.

        Returns
        -------
        ft.Row
            Row containing the themed icon and text controls.
        """

        row: ft.Row = ft.Row(
            spacing=theme.FOLDER_AND_ROUTE_CARD.SPACING_BETWEEN_ICON_AND_METRIC,
            controls=[
                ft.Icon(
                    icon=icon,
                    size=theme.FOLDER_AND_ROUTE_CARD.METRIC_ICON_SIZE,
                    color=theme.FOLDER_AND_ROUTE_CARD.METRIC_ICON_COLOR,
                ),
                ft.Text(
                    value=text,
                    size=theme.TEXT_SIZE.SUB,
                    color=theme.TEXT_COLOR.NORMAL,
                ),
            ],
        )

        return row

    def set_infos(self: Self, *, route_name: str, refreshing: bool) -> None:
        """Set the route name and optionally refresh the control.

        Parameters
        ----------
        route_name : str
            Route name displayed on the first line.
        refreshing : bool
            Whether to call the control's update method after setting the text.
            The control must be mounted when True.
        """

        self._route_name_text.value = f"{route_name:s}"

        if refreshing:
            self.update()
