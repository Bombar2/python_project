from tkinter import ttk
from frames.UI.ui import TextLocaleEnum, UIElementEnum
from purchases import PurchaseDict


class PurchaseButton:
    def __init__(self, parent, idx, button_id: UIElementEnum, locale:TextLocaleEnum = None):
        self._textUI = PurchaseDict(locale)
        self._button = self._create_purchase_button(parent, idx, button_id)


    def _create_purchase_button(self, parent, idx, button_id: UIElementEnum) -> ttk.Button:
        button = ttk.Button(parent,text=f"{idx}. {self._textUI.get_text_locale(button_id)} - "
                                        f"{self._textUI.get_ui_value(button_id)} бал(ов).")
        button.grid(row=idx, column=0, sticky="we", pady=2)
        return button

    def update_command(self, command):
        self._button.config(command=command)

    def update_state(self, state="normal"):
        self._button.config(state=state)