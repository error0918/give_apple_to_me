import threading
import tkinter
import time
from . import splash
from util import theme, controller


class MyButton:
    def __init__(
            self,
            root,
            on_click,
            text: str,
            subtext: str=None,
            background: str= theme.color_button1,
            foreground: str= theme.color_on_button1,
    ):
        self.frame = tkinter.Frame(
            root,
            cursor="hand2",
            background=background,
            relief="solid",
            borderwidth=2
        )
        self.text_label = tkinter.Label(
            self.frame,
            text=text,
            cursor="hand2",
            background=background,
            foreground=foreground,
            font=theme.font(size=40)
        )
        self.frame.bind("<Button-1>", lambda event, fun=on_click: fun())
        for widget in self.frame.winfo_children():
            widget.bind("<Button-1>", lambda event, fun=on_click: fun())

    def place(self, x: int, y: int, width: int, height: int):
        self.text_label.place(x=0, y=0, width=width-4, height=height-4)
        self.frame.place(
            x=x, y=y,
            width=width, height=height
        )

    def place_forget(self):
        self.frame.place_forget()


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
            asdf = action
            self.appbar_button.bind("<Button-1>", lambda event, fun=asdf: asdf())

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
            cursor="hand2",
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