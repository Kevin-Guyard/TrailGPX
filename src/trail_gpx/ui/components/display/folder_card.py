import flet as ft
from typing import Self

from ... import theme
from ..buttons import SmallIconButton, SmallIconButtonIcons


@ft.control()
class FolderCard(ft.Container):
    """Display a folder's name, route count, and options button."""

    def __init__(
        self: Self,
        *,
        folder_name: str,
        number_of_routes: int,
        on_click_options: ft.ControlEventHandler[ft.IconButton] | None = None,
        on_click_card: ft.ControlEventHandler[ft.Container] | None = None,
    ) -> None:
        """Initialize the folder card and its optional click handlers.

        Parameters
        ----------
        folder_name : str
            Folder name displayed on the first line, truncated if necessary.
        number_of_routes : int
            Number of routes displayed on the second line.
        on_click_options : ft.ControlEventHandler[ft.IconButton] or None, optional
            Callback invoked when the options button is clicked. Defaults to None.
        on_click_card : ft.ControlEventHandler[ft.Container] or None, optional
            Callback invoked when the card is clicked. Defaults to None.
        """

        # Keep references to update the labels without rebuilding the card.
        self._folder_name_text: ft.Text = ft.Text(
            color=theme.TEXT_COLOR.NORMAL,
            size=theme.TEXT_SIZE.NORMAL,
            weight=ft.FontWeight.BOLD,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
        )
        self._number_of_routes_text: ft.Text = ft.Text(
            color=theme.TEXT_COLOR.NORMAL,
            size=theme.TEXT_SIZE.SUB,
        )

        labels: ft.Column = ft.Column(
            expand=True,
            spacing=theme.FOLDER_AND_ROUTE_CARD.SPACING_BETWEEN_TWO_LINES,
            controls=[
                self._folder_name_text,
                self._number_of_routes_text,
            ],
        )
        folder_content: ft.Container = ft.Container(
            expand=True,
            content=ft.Row(
                spacing=theme.FOLDER_AND_ROUTE_CARD.SPACING_BETWEEN_ICON_AND_TEXT,
                controls=[
                    ft.Icon(
                        icon=ft.Icons.FOLDER,
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
            content=ft.Row(controls=[folder_content, options_button]),
        )

        # The control is not mounted during construction, so skip the page update.
        self.set_infos(
            folder_name=folder_name,
            number_of_routes=number_of_routes,
            refreshing=False,
        )

    def set_infos(
        self: Self,
        *,
        folder_name: str,
        number_of_routes: int,
        refreshing: bool,
    ) -> None:
        """Set the folder details and optionally refresh the control.

        Parameters
        ----------
        folder_name : str
            Folder name displayed on the first line.
        number_of_routes : int
            Number of routes displayed on the second line.
        refreshing : bool
            Whether to call the control's update method after setting the text.
            The control must be mounted when True.
        """

        self._folder_name_text.value = f"{folder_name:s}"
        self._number_of_routes_text.value = f"Routes: {number_of_routes:d}"

        if refreshing:
            self.update()
