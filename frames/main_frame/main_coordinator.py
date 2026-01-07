from frames.UI.ui import TextLocaleEnum
from frames.main_frame.main_root import MainActivity
from frames.main_frame.main_frame import MainFrame


class MainCoordinator:
    def __init__(self, locale: TextLocaleEnum = TextLocaleEnum.RUSSIAN, height: int = None, width:int = None):
        self._root = MainActivity(locale, height, width).get_root()
        self._main_frame = None

    def get_root(self):
        return self._root

    def get_main_frame(self):
        return self._main_frame

    def run(self):
        self._root.mainloop()

    def create_main_frame(self):
        self._main_frame = MainFrame(self._root).get_frame()
