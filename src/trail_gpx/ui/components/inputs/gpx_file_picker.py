import flet as ft
from pathlib import Path
from typing import Final, Self, cast

from ... import theme


_LABEL_STYLE_EMPTY: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.LIGHT,
    size=theme.TEXT_SIZE.NORMAL
)

_LABEL_STYLE_FILLED: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.NORMAL,
    size=theme.TEXT_SIZE.NORMAL
)

_LABEL_STYLE_ERROR: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.ERROR,
    size=theme.TEXT_SIZE.NORMAL
)

_ICON_COLOR_EMPTY: Final[str | ft.Colors] = theme.BORDER_COLOR.LIGHT
_ICON_COLOR_FILLED: Final[str | ft.Colors] = theme.BORDER_COLOR.NORMAL
_ICON_COLOR_ERROR: Final[str | ft.Colors] = theme.BORDER_COLOR.ERROR

_ERROR_MESSAGE_STYLE: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.ERROR,
    size=theme.TEXT_SIZE.ERROR
)

_FILENAME_STYLE: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.NORMAL,
    size=theme.TEXT_SIZE.NORMAL
)

_BORDER_EMPTY: Final[ft.OutlineInputBorder] = ft.OutlineInputBorder(
    border_radius=theme.GPX_FILE_PICKER.BORDER_RADIUS,
    side=ft.BorderSide(
        width=theme.GPX_FILE_PICKER.BORDER_WIDTH,
        color=theme.BORDER_COLOR.LIGHT
    ),
)

_BORDER_FILLED: Final[ft.OutlineInputBorder] = ft.OutlineInputBorder(
    border_radius=theme.GPX_FILE_PICKER.BORDER_RADIUS,
    side=ft.BorderSide(
        width=theme.GPX_FILE_PICKER.BORDER_WIDTH,
        color=theme.BORDER_COLOR.NORMAL
    ),
)

_BORDER_ERROR: Final[ft.OutlineInputBorder] = ft.OutlineInputBorder(
    border_radius=theme.GPX_FILE_PICKER.BORDER_RADIUS,
    side=ft.BorderSide(
        width=theme.GPX_FILE_PICKER.BORDER_WIDTH,
        color=theme.BORDER_COLOR.ERROR
    ),
)


@ft.control()
class GpxFilePicker(ft.TextField):
    """Display a read-only field for selecting and validating a GPX file."""

    def __init__(self: Self) -> None:
        """Initialize an empty GPX file field with a file picker callback."""
        self._selected_file: ft.FilePickerFile | None = None

        super().__init__(
            label="Select a GPX file",
            value=None,
            read_only=True,
            can_request_focus=False,
            enable_interactive_selection=False,
            label_style=_LABEL_STYLE_EMPTY,
            text_style=_FILENAME_STYLE,
            error_style=_ERROR_MESSAGE_STYLE,
            border={
                ft.ControlState.DEFAULT: _BORDER_EMPTY,
                ft.ControlState.ERROR: _BORDER_ERROR
            },
            width=float("inf"),
            bgcolor=theme.GPX_FILE_PICKER.BG_COLOR,
            content_padding=ft.Padding(
                left=theme.GPX_FILE_PICKER.PADDING_LEFT,
                top=theme.GPX_FILE_PICKER.PADDING_TOP,
                right=theme.GPX_FILE_PICKER.PADDING_RIGHT,
                bottom=theme.GPX_FILE_PICKER.PADDING_BOTTOM,
            ),
            prefix_icon=ft.Icon(
                icon=ft.Icons.FILE_UPLOAD_OUTLINED,
                size=theme.GPX_FILE_PICKER.ICON_SIZE,
                color=_ICON_COLOR_EMPTY
            ),
            on_click=self._pick_file,
        )

    @staticmethod
    def _validate_extension(file: ft.FilePickerFile) -> bool:
        """Check whether a file has a GPX extension, ignoring case.

        Parameters
        ----------
        file : ft.FilePickerFile
            File whose name is checked.

        Returns
        -------
        bool
            True if the file name ends with the GPX extension.
        """
        extension: str = Path(file.name).suffix.lstrip(".").lower()
        has_correct_extension: bool = extension == "gpx"

        return has_correct_extension

    def _apply_visual_state_no_selection(self: Self) -> None:
        """Restore field styles according to the current file selection."""
        self.label_style = (
            _LABEL_STYLE_EMPTY
            if self._selected_file is None
            else _LABEL_STYLE_FILLED
        )
        # The prefix icon is initialized as an ft.Icon in __init__.
        cast(ft.Icon, self.prefix_icon).color = (
            _ICON_COLOR_EMPTY
            if self._selected_file is None
            else _ICON_COLOR_FILLED
        )
        self.border = {
            ft.ControlState.DEFAULT: (
                _BORDER_EMPTY
                if self._selected_file is None
                else _BORDER_FILLED
            ),
            ft.ControlState.ERROR: _BORDER_ERROR
        }
        self.update()

    def _apply_visual_state_correct_selection(self: Self) -> None:
        """Apply valid-selection styles and refresh the field."""
        self.label_style = _LABEL_STYLE_FILLED
        cast(ft.Icon, self.prefix_icon).color = _ICON_COLOR_FILLED
        self.border = {
            ft.ControlState.DEFAULT: _BORDER_FILLED,
            ft.ControlState.ERROR: _BORDER_ERROR
        }
        self.update()

    def _apply_visual_state_error(self: Self) -> None:
        """Apply invalid-selection styles and refresh the field."""
        self.label_style = _LABEL_STYLE_ERROR
        cast(ft.Icon, self.prefix_icon).color = _ICON_COLOR_ERROR
        self.border = {
            ft.ControlState.DEFAULT: _BORDER_EMPTY,
            ft.ControlState.ERROR: _BORDER_ERROR
        }
        self.update()

    async def _pick_file(self: Self) -> None:
        """Open the file picker and update the selection and validation state.

        Notes
        -----
        Cancelling the dialog clears the error and preserves the current file.
        Selecting a file without a GPX extension clears the current selection.
        """
        selected_files: list[ft.FilePickerFile] = await ft.FilePicker().pick_files(
            dialog_title="Select a GPX file",
            allow_multiple=False,
        )

        if not selected_files:

            self.error = None
            self._apply_visual_state_no_selection()

            return

        selected_file: ft.FilePickerFile = selected_files[0]
        has_correct_extension: bool = self._validate_extension(selected_file)

        self._selected_file = (
            selected_file
            if has_correct_extension
            else None
        )
        self.value = (
            selected_file.name
            if has_correct_extension
            else None
        )
        self.error = (
            None
            if has_correct_extension
            else "Please select a GPX file."
        )

        if has_correct_extension:
            self._apply_visual_state_correct_selection()
        else:
            self._apply_visual_state_error()

    @property
    def selected_file(self: Self) -> ft.FilePickerFile | None:
        """Return the currently selected GPX file.

        Returns
        -------
        ft.FilePickerFile or None
            File accepted by extension validation, or None if none is selected.
        """
        return self._selected_file
