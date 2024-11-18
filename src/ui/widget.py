import threading
import tkinter
import time
from . import theme
from . import controller
from . import splash


class AppBar:
    def __init__(self, root, title, action=None):
        self.root = root
        self.action = action
        self.appbar = tkinter.Label(
            root,
            text = title,
            background=theme.color_primary,
            fg=theme.color_on_content,
            font=theme.font(size=50, bold=True)
        )
        if action is not None:
            self.appbar_button = tkinter.Label(
                root,
                text = "<",
                cursor="hand2",
                background=theme.color_primary,
                fg=theme.color_on_content,
                font=theme.font(size=60, bold=True)
            ) # 투명하게 하기 위해 가짜 버튼
            self.appbar_button.bind("<Button-1>", lambda event: action())

    def place(self):
        self.appbar.place(x=0, y=0, width=720, height=120)
        if self.action is not None:
            self.appbar_button.place(x=0, y=0, width=120, height=120)

    def place_forget(self):
        self.appbar.place_forget()
        if self.action is not None:
            self.appbar_button.place_forget()


class RestartBar:
    def __init__(self, root):
        self.root = root
        self.restart_bar = tkinter.Label(
            root,
            text = "처음으로",
            background=theme.color_container,
            fg=theme.color_on_container,
            font=theme.font(size=40)
        )
        self.restart_bar.bind("<Button-1>", lambda event: controller.change_screen(splash.Splash(root)))

    def place(self):
        self.restart_bar.place(x=0, y=1080-120, width=720, height=120)

    def place_forget(self):
        self.restart_bar.place_forget()


def toast(root, text: str, milli: int=1000):
    def toast_real():
        toast_label = tkinter.Label(
            root,
            text = text,
            wraplength=500,
            background=theme.color_toast,
            fg=theme.color_on_toast,
            font=theme.font(size=30),
            justify="center",
            padx=30, pady=10
        )
        toast_label.place(x=80, y=920, width=560)
        time.sleep(milli / 1000)
        toast_label.place_forget()

    threading.Thread(target = toast_real).start()