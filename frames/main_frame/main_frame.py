from tkinter import ttk


class MainFrame:
    def __init__(self, parent):
        self._frame = self._create_main_frame(parent)

    def _create_main_frame(self, parent) -> ttk.Frame:
        frame = ttk.Frame(parent, padding=10)
        frame.pack(fill="both", expand=True)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        return frame

    def get_frame(self):
        return self._frame