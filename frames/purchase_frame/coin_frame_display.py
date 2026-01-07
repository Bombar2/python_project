from tkinter import ttk

from frames.UI.ui import TextUI, TextLocaleEnum, UIElementEnum


class CoinFrameDisplay:
    def __init__(self, parent, locale: TextLocaleEnum = None):
        self._textUI = TextUI(locale)
        self._coin_label = None
        self._frame = self._create_coin_frame(parent)

    def _create_coin_frame(self, parent):
        frame = ttk.Frame(parent)
        frame.pack(fill="x", pady=5)
        ttk.Label(frame, text=self._textUI.get_text_locale(UIElementEnum.COINS_CURRENCY_TEXT), font=("Arial", 11)).pack(side="left")
        self._coin_label = ttk.Label(frame, text=self._textUI.get_ui_value(UIElementEnum.ZERO_BUTTON)
                                     ,font=("Arial", 11, "bold"), foreground="red")

        self._coin_label.pack(side="left", padx=(5, 0))
        #ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)

        return frame

    def update_coin(self, value: int):
        self._coin_label.config(text=str(value))

    def get_coin_value(self) -> int:
        return int(self._coin_label.cget("text"))

    def get_frame(self):
        return self._frame
