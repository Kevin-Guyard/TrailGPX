from collections.abc import Callable
import flet as ft
from typing import Final, Self

from ... import theme


_LABEL_STYLE_OFF_FOCUS_EMPTY: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.LIGHT,
    size=theme.TEXT_SIZE.NORMAL
)

_LABEL_STYLE_OFF_FOCUS_FILLED: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.NORMAL,
    size=theme.TEXT_SIZE.NORMAL
)

_LABEL_STYLE_OFF_FOCUS_ERROR: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.ERROR,
    size=theme.TEXT_SIZE.NORMAL
)

_LABEL_STYLE_ON_FOCUS: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.NORMAL,
    size=theme.TEXT_SIZE.NORMAL,
    weight=ft.FontWeight.BOLD
)

_HINT_STYLE: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.HINT,
    size=theme.TEXT_SIZE.NORMAL
)

_CONTENT_STYLE_VALID: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.NORMAL,
    size=theme.TEXT_SIZE.NORMAL
)

_CONTENT_STYLE_ERROR: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.ERROR,
    size=theme.TEXT_SIZE.NORMAL
)

_ERROR_MESSAGE_STYLE: Final[ft.TextStyle] = ft.TextStyle(
    color=theme.TEXT_COLOR.ERROR,
    size=theme.TEXT_SIZE.ERROR
)

_BORDER_EMPTY: Final[ft.OutlineInputBorder] = ft.OutlineInputBorder(
    border_radius=theme.TEXT_FIELD.BORDER_RADIUS,
    side=ft.BorderSide(
        color=theme.BORDER_COLOR.LIGHT,
        width=theme.TEXT_FIELD.BORDER_WIDTH_NOT_FOCUSED
    ),
)

_BORDER_FILLED: Final[ft.OutlineInputBorder] = ft.OutlineInputBorder(
    border_radius=theme.TEXT_FIELD.BORDER_RADIUS,
    side=ft.BorderSide(
        color=theme.BORDER_COLOR.NORMAL,
        width=theme.TEXT_FIELD.BORDER_WIDTH_NOT_FOCUSED
    ),
)

_BORDER_ERROR: Final[ft.OutlineInputBorder] = ft.OutlineInputBorder(
    border_radius=theme.TEXT_FIELD.BORDER_RADIUS,
    side=ft.BorderSide(
        color=theme.BORDER_COLOR.ERROR,
        width=theme.TEXT_FIELD.BORDER_WIDTH_NOT_FOCUSED
    ),
)

_BORDER_FOCUSED: Final[ft.OutlineInputBorder] = ft.OutlineInputBorder(
    border_radius=theme.TEXT_FIELD.BORDER_RADIUS,
    side=ft.BorderSide(
        color=theme.BORDER_COLOR.NORMAL,
        width=theme.TEXT_FIELD.BORDER_WIDTH_FOCUSED
    ),
)

@ft.control()
class TextField(ft.TextField):
    """A themed text field with focus feedback and optional validation."""

    def __init__(
        self: Self,
        *,
        label: str,
        value: str | None = None,
        hint_text: str | None = None,
        max_length: int | None = None,
        validator: Callable[[str], str | None] | None = None
    ) -> None:
        """Initialize the field and validate its initial value.

        Parameters
        ----------
        label : str
            Label displayed for the field.
        value : str or None, optional
            Initial text. None is treated as empty during validation.
        hint_text : str or None, optional
            Hint displayed when the field is empty.
        max_length : int or None, optional
            Maximum number of characters allowed, or None for no limit.
        validator : callable or None, optional
            Function receiving the current text and returning an error message
            for invalid input or None for valid input.
        """

        self._validator: Callable[[str], str | None] | None = validator
        self._is_focused: bool = False

        super().__init__(
            label=label,
            value=value,
            hint_text=hint_text,
            max_length=max_length,
            width=float("inf"),
            label_style=_LABEL_STYLE_OFF_FOCUS_EMPTY,
            hint_style=_HINT_STYLE,
            text_style=_CONTENT_STYLE_VALID,
            error_style=_ERROR_MESSAGE_STYLE,
            bgcolor=theme.TEXT_FIELD.BG_COLOR,
            content_padding=ft.Padding(
                left=theme.TEXT_FIELD.PADDING_LEFT,
                top=theme.TEXT_FIELD.PADDING_TOP,
                right=theme.TEXT_FIELD.PADDING_RIGHT,
                bottom=theme.TEXT_FIELD.PADDING_BOTTOM,
            ),
            border={
                ft.ControlState.DEFAULT: _BORDER_EMPTY,
                ft.ControlState.FOCUSED: _BORDER_FOCUSED,
                ft.ControlState.ERROR: _BORDER_ERROR
            },
            on_focus=self._on_focus,
            on_blur=self._on_blur
        )

        # The control is not mounted yet, so only update its local state.
        self.validate(refreshing=False)

    def _apply_visual_state(self: Self, refreshing: bool) -> None:
        """Apply styles based on focus, content, and validation state.

        Parameters
        ----------
        refreshing : bool
            Whether to send the updated styles to the mounted control.
        """

        has_content: bool = bool(self.value)
        has_error: bool = self.error is not None

        # Focus styling takes precedence over validation feedback while editing.
        if self._is_focused:
            self.label_style = _LABEL_STYLE_ON_FOCUS
        elif has_error:
            self.label_style = _LABEL_STYLE_OFF_FOCUS_ERROR
        elif has_content:
            self.label_style = _LABEL_STYLE_OFF_FOCUS_FILLED
        else:
            self.label_style = _LABEL_STYLE_OFF_FOCUS_EMPTY

        self.text_style = (
            _CONTENT_STYLE_ERROR
            if has_error and not self._is_focused
            else _CONTENT_STYLE_VALID
        )

        self.border = {
            ft.ControlState.DEFAULT: (
                _BORDER_FILLED
                if has_content
                else _BORDER_EMPTY
            ),
            ft.ControlState.FOCUSED: _BORDER_FOCUSED,
            ft.ControlState.ERROR: _BORDER_ERROR
        }

        if refreshing:
            self.update()

    def validate(self: Self, refreshing: bool) -> bool:
        """Validate the current text and update the error and visual state.

        Parameters
        ----------
        refreshing : bool
            Whether to send the updated state to the mounted control.

        Returns
        -------
        bool
            True if no validator is configured or the validator returns None;
            False if it returns an error message.
        """

        message: str | None = (
            self._validator(self.value or "")
            if self._validator is not None
            else None
        )

        self.error = message
        self._apply_visual_state(refreshing=refreshing)

        return message is None

    def _on_focus(self: Self) -> None:
        """Clear the displayed error and apply the focused styles."""

        self._is_focused = True
        self.error = None
        self._apply_visual_state(refreshing=True)

    def _on_blur(self: Self) -> None:
        """Validate the current text when the field loses focus."""

        self._is_focused = False
        self.validate(refreshing=True)
