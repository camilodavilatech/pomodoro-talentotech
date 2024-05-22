from tkinter import Frame, Label, Button, ttk
from consts import PINK, YELLOW, RED, FONT_NAME


class Settings(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.settings_default = {"long_timer": 20, "short_timer": 5, "work_timer": 1}

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
            values=["1", "2", "3", "4", "5"],
            width=25,
            height=10,
            font=(FONT_NAME, 18),
        )
        work_select.pack(pady=10)

        Label(self, text="Long timer", font=(FONT_NAME, 18)).pack(pady=5)
        short_select = ttk.Combobox(
            self,
            values=["5", "10", "15", "20", "25", "30", "35", "40"],
            width=25,
            height=10,
            font=(FONT_NAME, 18),
        )
        short_select.pack(pady=10)

        Label(self, text="Short timer", font=(FONT_NAME, 18)).pack(pady=5)
        long_select = ttk.Combobox(
            self,
            values=["10", "20", "30", "40", "50"],
            width=25,
            height=10,
            font=(FONT_NAME, 18),
        )
        long_select.pack(pady=10)

    def save_settings(self, new_settings):
        pass

    def onchange_select(self, value, key):
        new_settings = self.settings_default.update(key, value)

        self.save_settings(new_settings)
