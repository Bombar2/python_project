from tkinter import ttk, Tk

from frames.UI.ui import TextLocaleEnum
from frames.status_frame.status_frame_coordinator import StatusFrameCoordinator
from frames.numeric_keypad.numeric_keypad_coordinator import NumericKeypadCoordinator
from frames.purchase_frame.purchase_coordinator import PurchaseCoordinator
from frames.main_frame.main_coordinator import MainCoordinator


class Factory:
    @staticmethod
    def create_status_frame_default(parent: ttk.Frame, locale: TextLocaleEnum = TextLocaleEnum.RUSSIAN) -> StatusFrameCoordinator:
        coordinator = StatusFrameCoordinator(parent, locale)
        return coordinator

    @staticmethod
    def create_numeric_keypad_default(parent: ttk.Frame, locale: TextLocaleEnum = TextLocaleEnum.RUSSIAN) -> NumericKeypadCoordinator:
        coordinator = NumericKeypadCoordinator(parent, locale)
        return coordinator

    @staticmethod
    def create_purchases_frame_default(parent: ttk.Frame, locale: TextLocaleEnum = TextLocaleEnum.RUSSIAN) -> PurchaseCoordinator:
        coordinator = PurchaseCoordinator(parent, locale)
        return coordinator

    @staticmethod
    def create_main_activity_default(height: int = 600, width: int = 500, locale: TextLocaleEnum = TextLocaleEnum.RUSSIAN) -> MainCoordinator:
        coordinator = MainCoordinator(locale, height, width)
        return coordinator
