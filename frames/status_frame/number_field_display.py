from tkinter import ttk
from typing import Optional

from frames.UI.ui import TextUI, UIElementEnum, TextLocaleEnum


class NumberFieldDisplay:
    def __init__(self, parent: ttk.LabelFrame, styles = None, locale: Optional[TextLocaleEnum] = None):
        """parent = StatusDisplayFrame"""
        self._text_ui = TextUI(locale)
        self._number_field = None

        self._frame = self._create_enter_number_field(parent, styles)


    def _create_enter_number_field(self, parent, styles = None) -> ttk.Frame:
        frame = ttk.Frame(parent, relief="solid", borderwidth=1)
        frame.grid(column=0, row=4, columnspan=2, sticky="we", pady=(0, 5))

        self._number_field = ttk.Label(frame, text=self._text_ui.get_ui_value(UIElementEnum.NUMBER_FIELD),
                                      font=("Arial", 20, "bold"),
                                      background="white",
                                      width=10)
        self._number_field.pack(padx=10, pady=10)

        return frame

    def update_number_field(self, value: str) -> None:
        self._number_field.configure(text=value)

    def get_number_field_text(self) -> str:
        return self._number_field.cget("text")