from frames.UI.ui import TextLocaleEnum
from frames.purchase_frame.purchases_display import PurchasesDisplay
from frames.purchase_frame.coin_frame_display import CoinFrameDisplay
from frames.purchase_frame.shop_frame_display import ShopDisplay


class PurchaseCoordinator:
    def __init__(self, parent, locale: TextLocaleEnum = None):
        self._parent = parent

        self._purchases_frame = PurchasesDisplay(self._parent, locale).get_frame()
        self._coin_frame  = CoinFrameDisplay(self._purchases_frame, locale)
        self._shop_frame = None

    def create_shop_buttons(self, purchases_dict, locale: TextLocaleEnum = None):
        self._shop_frame = ShopDisplay(self._purchases_frame, purchases_dict, locale)

    def update_coin(self, value:int):
        if self._coin_frame.get_coin_value() != value:
            self._coin_frame.update_coin(value)

    def update_button_state(self, coin: int):
        self._shop_frame.update_purchase_buttons(coin)
