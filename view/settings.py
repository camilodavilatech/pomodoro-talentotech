from tkinter import Frame, Label, Button, ttk
from consts import PINK, YELLOW, RED, FONT_NAME
from utils.settings import get_settings, saved_settings


class Settings(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.settings_default = get_settings()

        label = Label(
            self,
            text="Settings",
            bg=YELLOW,
            fg=PINK,
            font=(FONT_NAME, 30, "bold"),
        )
        label.pack(pady=20)

        self.render()

    def render(self):
        Label(self, text="Work timer", font=(FONT_NAME, 18)).pack(pady=5)
        work_select = ttk.Combobox(
            self,
            values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            width=25,
            height=10,
            font=(FONT_NAME, 18),
        )
        work_select.pack(pady=10)
        # definir un valor por defecto
        # cada vez que el valor del diccionario cambier el valor por defecto cambiara
        work_select.set(self.settings_default["work"])
        # detectar el evento
        # actualizar la información
        work_select.bind(
            "<<ComboboxSelected>>",
            lambda e: self.onchange_select(work_select.get(), "work"),
        )

        Label(self, text="Long timer", font=(FONT_NAME, 18)).pack(pady=5)
        short_select = ttk.Combobox(
            self,
            values=["5", "10", "15", "20", "25", "30", "35", "40"],
            width=25,
            height=10,
            font=(FONT_NAME, 18),
        )
        short_select.pack(pady=10)
        short_select.set(self.settings_default["short_break"])
        short_select.bind(
            "<<ComboboxSelected>>",
            lambda e: self.onchange_select(short_select.get(), "short_break"),
        )

        Label(self, text="Short timer", font=(FONT_NAME, 18)).pack(pady=5)
        long_select = ttk.Combobox(
            self,
            values=["10", "20", "30", "40", "50"],
            width=25,
            height=10,
            font=(FONT_NAME, 18),
        )
        long_select.pack(pady=10)
        long_select.set(self.settings_default["long_break"])
        long_select.bind(
            "<<ComboboxSelected>>",
            lambda e: self.onchange_select(long_select.get(), "long_break"),
        )

    def onchange_select(self, value, key):
        print(self.settings_default)
        self.settings_default[key] = int(value)
        print(self.settings_default)

        saved_settings(self.settings_default)
