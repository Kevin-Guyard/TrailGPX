from typing import Final, Self

import flet as ft

from ... import theme


_TEXT_STYLE: Final[ft.TextStyle] = ft.TextStyle(
    size=theme.TEXT_SIZE.NORMAL,
    color=theme.TEXT_COLOR.NORMAL,
)

_SECTION_TITLE_TEXT_STYLE: Final[ft.TextStyle] = ft.TextStyle(
    size=theme.TEXT_SIZE.IMPORTANT,
    color=theme.TEXT_COLOR.NORMAL,
    weight=ft.FontWeight.BOLD,
)


@ft.control()
class GpxDetailInfosDisplay(ft.Column):
    """Display route metrics and the download status of its map."""

    def __init__(
        self: Self,
        *,
        route_name: str,
        distance_km: float,
        elevation_gain_m: int,
        elevation_loss_m: int,
        map_size_bytes: float,
    ) -> None:
        """Initialize the route information controls.

        Parameters
        ----------
        route_name : str
            Name of the route.
        distance_km : float
            Route distance in kilometers.
        elevation_gain_m : int
            Total elevation gain in meters.
        elevation_loss_m : int
            Total elevation loss in meters.
        map_size_bytes : float
            Downloaded map size in bytes. Nonpositive values indicate that
            the map is not downloaded.
        """
        self._route_name_text: ft.Text = ft.Text(
            expand=True,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
            style=_TEXT_STYLE,
        )
        self._is_route_map_downloaded_text: ft.Text = ft.Text(style=_TEXT_STYLE)

        super().__init__(
            spacing=theme.GPX_DETAIL_INFOS_DISPLAY.SPACING_AFTER_TITLE,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value="Route information", style=_SECTION_TITLE_TEXT_STYLE),
                ft.Column(
                    spacing=theme.GPX_DETAIL_INFOS_DISPLAY.SPACING_BETWEEN_TWO_LINES,
                    controls=[
                        self._construct_row(
                            icon=ft.Icons.LABEL_OUTLINED,
                            label="Name: ",
                            value=self._route_name_text,
                        ),
                        self._construct_row(
                            icon=ft.Icons.STRAIGHTEN,
                            label="Distance: ",
                            value=ft.Text(value=f"{distance_km:.1f} km", style=_TEXT_STYLE),
                        ),
                        self._construct_row(
                            icon=ft.Icons.TRENDING_UP,
                            label="Elevation gain: ",
                            value=ft.Text(value=f"{elevation_gain_m:d} m", style=_TEXT_STYLE),
                        ),
                        self._construct_row(
                            icon=ft.Icons.TRENDING_DOWN,
                            label="Elevation loss: ",
                            value=ft.Text(value=f"{elevation_loss_m:d} m", style=_TEXT_STYLE),
                        ),
                        self._construct_row(
                            icon=ft.Icons.CLOUD_OFF,
                            label="Map downloaded: ",
                            value=self._is_route_map_downloaded_text,
                        ),
                    ],
                ),
            ],
        )

        self.set_infos(
            refreshing=False,
            route_name=route_name,
            map_size_bytes=map_size_bytes,
        )

    @staticmethod
    def _construct_row(icon: ft.IconData, label: str, value: ft.Text) -> ft.Row:
        """Build an information row with an icon, a label, and a value.

        Parameters
        ----------
        icon : ft.IconData
            Icon displayed before the label.
        label : str
            Label displayed in bold before the value.
        value : ft.Text
            Text control displaying the information value.

        Returns
        -------
        ft.Row
            Row containing the icon and the label-value pair.
        """
        row: ft.Row = ft.Row(
            spacing=theme.GPX_DETAIL_INFOS_DISPLAY.SPACING_BETWEEN_ICON_AND_TEXT,
            controls=[
                ft.Icon(
                    icon=icon,
                    size=theme.GPX_DETAIL_INFOS_DISPLAY.ICON_SIZE,
                    color=theme.GPX_DETAIL_INFOS_DISPLAY.ICON_COLOR,
                ),
                ft.Row(
                    expand=True,
                    spacing=0,
                    controls=[
                        ft.Text(
                            value=label,
                            weight=ft.FontWeight.BOLD,
                            size=theme.TEXT_SIZE.NORMAL,
                            color=theme.TEXT_COLOR.NORMAL,
                        ),
                        value,
                    ],
                ),
            ],
        )

        return row

    def set_infos(
        self: Self,
        *,
        refreshing: bool,
        route_name: str | None = None,
        map_size_bytes: float | None = None,
    ) -> None:
        """Update the supplied route details and optionally refresh the control.

        Parameters
        ----------
        refreshing : bool
            Whether to push the control changes to the page immediately.
            The control must be mounted when this is True.
        route_name : str or None, optional
            New route name. If None, keep the current name.
        map_size_bytes : float or None, optional
            New downloaded map size in bytes. Nonpositive values indicate
            that the map is not downloaded. If None, keep the current status.
        """
        if route_name is not None:
            self._route_name_text.value = route_name

        if map_size_bytes is not None:
            # Use decimal megabytes to match the displayed MB unit.
            self._is_route_map_downloaded_text.value = (
                f"Yes ({map_size_bytes / (1000 ** 2):.1f} MB)"
                if map_size_bytes > 0.0
                else "No"
            )

        if refreshing:
            self.update()
