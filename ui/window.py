from tkinter import Tk, Frame, Button
from consts import YELLOW
from view import Analytics, Home, Settings


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("Pomodoro App")
        self.geometry("450x420")

        self.container = Frame(self)
        self.container.config(bg=YELLOW)
        self.container.pack(fill="both", expand=True)

        # views
        self.frames = {}
        self.current_frame = "home"

        self.add_view(Home, "home")
        self.add_view(Analytics, "analytics")
        self.add_view(Settings, "settings")

        self.show_view("home")
        self.render()

    def render(self):
        view_settings = Button(
            self.container,
            text="settings",
            background="black",
            foreground="white",
            borderwidth=0,
            padx=10,
            pady=10,
            command=lambda: (
                self.show_view("settings")
                if self.current_frame == "home"
                else self.show_view("home")
            ),
        )
        view_settings.place(x=10, y=10)

    def show_view(self, name):
        self.current_frame = name
        # ocultar la vista actual
        for frame in self.frames.values():
            frame.pack_forget()

        # show new frame
        view = self.frames.get(name)

        if view:
            view.pack()

    def add_view(self, view, name):
        frame: Frame = view(self.container, self)

        self.frames[name] = frame
        frame.pack(fill="both", expand=True)
        frame.config(bg=YELLOW)
