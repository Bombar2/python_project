from tkinter import ttk
from frames.UI.ui import TextUI, TextLocaleEnum, UIElementEnum


class PurchasesDisplay:
    def __init__(self, parent: ttk.Frame, locale: TextLocaleEnum = None):
        self._textUI = TextUI(locale)
        self._frame = self._create_purchases_frame(parent)

    def _create_purchases_frame(self, parent: ttk.Frame) -> ttk.LabelFrame:
        frame = ttk.LabelFrame(parent, text=self._textUI.get_text_locale(UIElementEnum.GAME_CURRENCY_TEXT), padding=10)
        frame.grid(column=1, row=0, rowspan=2, sticky="nsew")

        ttk.Label(frame, text=self._textUI.get_text_locale(UIElementEnum.GAME_CURRENCY),
                  font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 10))

        return frame

    def get_frame(self) -> ttk.LabelFrame:
        return self._frame
