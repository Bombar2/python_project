from tkinter import ttk
from typing import Optional

from frames.UI.ui import TextUI, UIElementEnum, TextLocaleEnum


class StatusDisplay:
    """Класс создания статусного виджета."""
    def __init__(self, parent: ttk.LabelFrame, styles = None, locale:TextLocaleEnum = None):
        self._text_ui = TextUI(locale)
        self._health_label = None
        self._attempt_label = None

        self._frame = self._create_status_frame(parent, styles)


    def _create_status_frame(self, parent, styles = None) -> ttk.LabelFrame:

        frame = ttk.LabelFrame(parent, text=self._text_ui.get_text_locale(UIElementEnum.STATUS_FRAME_TEXT), padding=15)
        frame.grid(column=0, row=0, sticky="nsew", padx=(0, 5), pady=(0, 5))

        frame.grid_columnconfigure(1, weight=1)

        ttk.Label(frame, text=self._text_ui.get_text_locale(UIElementEnum.STATUS_HEALTH),
                  font=("Arial", 11)).grid(column=0, row=0, sticky="w", pady=5)

        self._health_label = ttk.Label(frame, text="",
                                      font=("Arial", 14),
                                      foreground="red")
        self._health_label.grid(column=1, row=0, sticky="w", padx=(10, 0), pady=5)

        ttk.Label(frame, text=self._text_ui.get_text_locale(UIElementEnum.STATUS_ATTEMPT),
                  font=("Arial", 11)).grid(column=0, row=1, sticky="w", pady=5)

        self._attempt_label = ttk.Label(frame, text=self._text_ui.get_ui_value(UIElementEnum.STATUS_ATTEMPT),
                                       font=("Arial", 14),
                                       foreground="blue")
        self._attempt_label.grid(column=1, row=1, sticky="w", padx=(10, 0), pady=5)

        ttk.Separator(frame, orient="horizontal").grid(
            column=0, row=2, columnspan=2, sticky="we", pady=15)

        ttk.Label(frame, text=self._text_ui.get_text_locale(UIElementEnum.ENTER_NUMBER)
                  , font=("Arial", 12, "bold")).grid(column=0, row=3, columnspan=2, sticky="w", pady=(0, 10))

        ttk.Label(frame, text=self._text_ui.get_text_locale(UIElementEnum.NUMBER_FIELD)
                  , font=("Arial", 9), foreground="gray").grid(column=0, row=5, columnspan=2, sticky="w")

        return frame

    def update_status_health(self, value: int) -> None:
        """Функция обновления информации по оставшимся жизням"""
        self._health_label.config(text=str(self._text_ui.get_ui_value(UIElementEnum.STATUS_HEALTH) * value))

    def update_status_attempt(self, value: str) -> None:
        self._attempt_label.config(text=value)

    def get_frame(self) -> ttk.LabelFrame:
        return self._frame