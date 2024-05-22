from tkinter import Frame, Label, PhotoImage, Button
from consts import (
    YELLOW,
    GREEN,
    RED,
    PINK,
    FONT_NAME,
    SHORT_BREAK_MIN,
    WORK_MIN,
    LONG_BREAK_MIN,
)


class Home(Frame):
    def __init__(self, parent: Frame, controller):
        super().__init__(parent)

        self.controller = controller
        self.image = PhotoImage(file="tomato.png")

        self.title_label = Label(
            self,
            text="Pomodoro",
            background=YELLOW,
            foreground=RED,
            font=(FONT_NAME, 30, "bold"),
        )
        self.image_label = Label(self, image=self.image, bg=YELLOW)
        self.timer_label = Label(
            self, text="00:00", foreground=RED, font=(FONT_NAME, 40, "bold")
        )

        self.start_button = Button(
            self,
            text="Start Timer",
            background=GREEN,
            foreground="black",
            font=(FONT_NAME, 15, "bold"),
            width=30,
            pady=10,
            command=self.start_timer,
        )
        self.reset_button = Button(
            self,
            text="Reset Timer",
            background="black",
            foreground="white",
            font=(FONT_NAME, 15, "bold"),
            width=30,
            pady=10,
            command=self.rest_timer,
        )

        self.check_mark = Label(text="")

        self.render()

        self.timer = None
        self.reps = 0

    def render(self):
        self.title_label.pack(pady=10)
        self.image_label.pack_configure(anchor="center")

        self.timer_label.place(relx=0.5, rely=0.58, anchor="center")
        self.start_button.pack(pady=10)

    def rest_timer(self):
        self.after_cancel(self.timer)

        self.timer_label.config(text="00:00")
        self.title_label.config(text="Pomodoro")
        self.check_mark.config(text="")
        self.start_button.pack(pady=10)
        self.reset_button.pack_forget()

        self.reps = 0

    def start_timer(self):
        """
        Incrementa la variables repeticiones cada vez que se corre
        la funcion start_timer
        """
        self.reps += 1

        """
            Se multiplica por 60 cada valor de las constantes
            para convertirlos a segundos
        """
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        self.start_button.pack_forget()
        self.reset_button.pack(pady=10)

        if self.reps % 8 == 0:
            self.count_down(long_break_sec)
            self.title_label.config(text="Break", fg=RED)
        elif self.reps % 2 == 0:
            self.count_down(short_break_sec)
            self.title_label.config(text="Break", fg="pink")
        else:
            self.count_down(work_sec)
            self.title_label.config(text="Work", fg=GREEN)

    def count_down(self, count: int):
        count_min = count // 60
        count_seg = count % 60

        if count_seg < 10:
            count_seg = f"0{count_seg}"

        self.timer_label.config(text=f"{count_min}:{count_seg}")

        if count > 0:
            self.timer = self.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()

            marks = ""
            """
             TODO: resolved a bug
            """
            work_session = self.reps // 0

            for _ in range(work_session):
                marks += "✅"

            self.check_mark.config(text=marks)
