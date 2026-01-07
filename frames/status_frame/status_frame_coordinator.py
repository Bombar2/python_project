from frames.UI.ui import TextLocaleEnum
from frames.status_frame.status_display import StatusDisplay
from frames.status_frame.number_field_display import NumberFieldDisplay

class StatusFrameCoordinator:
    def __init__(self, parent, locale: TextLocaleEnum = TextLocaleEnum.RUSSIAN):
        self._parent = parent

        self._status_currency_display = StatusDisplay(self._parent, locale)
        self._number_field_currency_display = NumberFieldDisplay(self._status_currency_display.get_frame(), locale)


    def update_currency_status_health(self, value: int) -> None:
        self._status_currency_display.update_status_health(value)

    def update_currency_status_attempts(self, value: int) -> None:
        self._status_currency_display.update_status_attempt(str(value))

    def update_currency_number_field(self, value: int) -> None:
        self._number_field_currency_display.update_number_field(str(value))

    def get_currency_number_field_text(self) -> str:
        return self._number_field_currency_display.get_number_field_text()