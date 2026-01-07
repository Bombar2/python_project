from frames.UI.ui import TextLocaleEnum
from frames.numeric_keypad.numeric_keypad_display import NumericKeypadDisplay


class NumericKeypadCoordinator:
    def __init__(self, parent, locale: TextLocaleEnum = TextLocaleEnum.RUSSIAN):
        self._parent = parent

        self._numeric_keypad_currency_display = NumericKeypadDisplay(self._parent, locale)


    def show_hint(self, number, status: bool = True):
        self._numeric_keypad_currency_display.show_hint(number, status)

    def reset_hint(self):
        self._numeric_keypad_currency_display.reset_hint()

    def set_buttons_callback(self, callbacks):
        self._numeric_keypad_currency_display.set_buttons_callback(callbacks)