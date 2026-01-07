from tkinter import ttk

from frames.UI.ui import TextLocaleEnum, UIElementEnum
from purchases import PurchaseDict
from frames.purchase_frame.purchase_button import PurchaseButton


class ShopDisplay:
    def __init__(self, parent, purchases_dict, locale: TextLocaleEnum = None):
        self._textUI = PurchaseDict(locale)
        self._frame = self._create_shop_frame(parent)
        self._purchases_buttons_dict = self._create_purchases_buttons_dict(self._frame, purchases_dict)


    def _create_shop_frame(self, parent):
        frame = ttk.Frame(parent)
        frame.pack(fill="both", expand=True)

        frame.grid_columnconfigure(0, weight=1)

        return frame

    def _create_purchases_buttons_dict(self, parent, purchases_dict):

        purchases_buttons_dict = {}

        for i, (button_id, command) in enumerate(purchases_dict.items()):
            button = PurchaseButton(parent, i, button_id, self._textUI.get_locale())
            if button_id == UIElementEnum.NUMERIC_BUTTON:
                button.update_command(lambda idx=button_id: command(idx))
            else:
                button.update_command(lambda idx=button_id: command(idx))
            purchases_buttons_dict[button_id] = button

        return purchases_buttons_dict

    def update_purchase_buttons(self, coin: int):

        for button_id, button in self._purchases_buttons_dict.items():
            if int(self._textUI.get_ui_value(button_id)) > coin:
                button.update_state("disabled")
            else:
                button.update_state()