import flet as ft
from typing import Final, Self

from ... import theme


_TITLE_TEXT_STYLE: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.NORMAL,
    size=theme.TEXT_SIZE.IMPORTANT,
    weight=ft.FontWeight.BOLD,
)

METRIC_TEXT_STYLE: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.NORMAL,
    size=theme.TEXT_SIZE.NORMAL,
)


@ft.control()
class GpxInfosDisplay(ft.Column):
    """Display a GPX track's distance, elevation gain, and elevation loss."""

    def __init__(
        self: Self,
        *,
        distance_km: float | None = None,
        elevation_gain_m: int | None = None,
        elevation_loss_m: int | None = None,
    ) -> None:
        """Initialize the metric rows with the supplied track information.

        Parameters
        ----------
        distance_km : float or None, optional
            Track distance in kilometers, displayed with one decimal place.
            None is displayed as 0.0 km. Defaults to None.
        elevation_gain_m : int or None, optional
            Total elevation gain in meters. None is displayed as 0 m.
            Defaults to None.
        elevation_loss_m : int or None, optional
            Total elevation loss in meters. None is displayed as 0 m.
            Defaults to None.
        """
        # Keep references to update metric values without rebuilding the layout.
        self._distance_text: ft.Text = ft.Text(style=METRIC_TEXT_STYLE)
        self._elevation_gain_text: ft.Text = ft.Text(style=METRIC_TEXT_STYLE)
        self._elevation_loss_text: ft.Text = ft.Text(style=METRIC_TEXT_STYLE)

        super().__init__(
            spacing=theme.GPX_INFOS_DISPLAY.SPACING_AFTER_TITLE,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value="GPX track information",
                    style=_TITLE_TEXT_STYLE,
                ),
                ft.Row(
                    spacing=theme.GPX_INFOS_DISPLAY.SPACING_BETWEEN_METRIC_BLOCS,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self._generate_metric_info_row(
                            icon=ft.Icons.STRAIGHTEN,
                            text=self._distance_text,
                        ),
                        self._generate_metric_info_row(
                            icon=ft.Icons.TRENDING_UP,
                            text=self._elevation_gain_text,
                        ),
                        self._generate_metric_info_row(
                            icon=ft.Icons.TRENDING_DOWN,
                            text=self._elevation_loss_text,
                        ),
                    ],
                ),
            ],
        )

        # The control is not mounted during construction, so skip the page update.
        self.set_infos(
            distance_km=distance_km,
            elevation_gain_m=elevation_gain_m,
            elevation_loss_m=elevation_loss_m,
            refreshing=False,
        )

    def set_infos(
        self: Self,
        *,
        distance_km: float | None,
        elevation_gain_m: int | None,
        elevation_loss_m: int | None,
        refreshing: bool,
    ) -> None:
        """Set all displayed metrics and optionally refresh the control.

        Parameters
        ----------
        distance_km : float or None
            Track distance in kilometers, displayed with one decimal place.
            None is displayed as 0.0 km.
        elevation_gain_m : int or None
            Total elevation gain in meters. None is displayed as 0 m.
        elevation_loss_m : int or None
            Total elevation loss in meters. None is displayed as 0 m.
        refreshing : bool
            Whether to call the control's update method after setting the text.
            The control must be mounted when True.
        """

        self._distance_text.value = (
            f"{distance_km:.1f} km" if distance_km is not None else "—"
        )
        self._elevation_gain_text.value = (
            f"{elevation_gain_m:d} m" if elevation_gain_m is not None else "—"
        )
        self._elevation_loss_text.value = (
            f"{elevation_loss_m:d} m" if elevation_loss_m is not None else "—"
        )

        if refreshing:
            self.update()

    @staticmethod
    def _generate_metric_info_row(icon: ft.IconData, text: ft.Text) -> ft.Row:
        """Build a compact row containing a metric icon and its text control.

        Parameters
        ----------
        icon : ft.IconData
            Icon identifying the metric.
        text : ft.Text
            Existing text control displaying the metric value and unit.

        Returns
        -------
        ft.Row
            Row containing the themed icon followed by the supplied text control.
        """
        row: ft.Row = ft.Row(
            spacing=theme.GPX_INFOS_DISPLAY.SPACING_BETWEEN_ICON_AND_METRIC,
            tight=True,
            controls=[
                ft.Icon(
                    icon=icon,
                    size=theme.GPX_INFOS_DISPLAY.ICON_SIZE,
                    color=theme.GPX_INFOS_DISPLAY.ICON_COLOR,
                ),
                text,
            ],
        )

        return row
