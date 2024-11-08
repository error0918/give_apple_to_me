import tkinter
from . import controller
from . import screen
from . import select1
from . import theme
from . import widget


class Select2a(screen.Screen): # 가전
    def __init__(self, root):
        self.root = root
        self.appbar = widget.AppBar(root, title="가전", action=lambda : controller.change_screen(select1.Select1(root)))

    def show(self):
        self.appbar.place()

    def hide(self):
        self.appbar.place_forget()


class Select2b(screen.Screen): # 음식물
    def __init__(self, root):
        self.root = root
        self.appbar = widget.AppBar(root, title="음식물", action=lambda : controller.change_screen(select1.Select1(root)))

        self.wait_a_minute = tkinter.Label(
            root,
            text = "잠깐! 곰팡이가 피었나요?",
            background=theme.color_background,
            fg=theme.color_on_background,
            font=theme.font(size=55, bold=True)
        )

        def command_wait_no(): pass
        self.wait_no_button = tkinter.Button(
            root,
            text = "아니요",
            padx=20, pady=10,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=1,
            font=theme.font(size=40),
            command=command_wait_no
        )

        def command_wait_yes():
            widget.toast(root, text="상하거나 곰팡이가 핀 쓰레기는 일반 쓰레기로 분류됩니다.")
            # Todo
        self.wait_yes_button = tkinter.Button(
            root,
            text = "예",
            padx=20, pady=10,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=1,
            font=theme.font(size=40),
            command=command_wait_yes
        )

    def show(self):
        self.appbar.place()
        self.wait_a_minute.place(x=0, y=500, width=720, height=80)
        self.wait_no_button.place(x=100, y=620, width=240, height=80)
        self.wait_yes_button.place(x=380, y=620, width=240, height=80)

    def hide(self):
        self.appbar.place_forget()
        self.wait_a_minute.place_forget()
        self.wait_no_button.place_forget()
        self.wait_yes_button.place_forget()


class Select2c(screen.Screen): # 생활 쓰레기
    def __init__(self, root):
        self.root = root
        self.appbar = widget.AppBar(root, title="생활 쓰레기", action=lambda : controller.change_screen(select1.Select1(root)))

    def show(self):
        self.appbar.place()

    def hide(self):
        self.appbar.place_forget()


class Select2d(screen.Screen): # 기타
    def __init__(self, root):
        self.root = root
        self.appbar = widget.AppBar(root, title="기타", action=lambda : controller.change_screen(select1.Select1(root)))

    def show(self):
        self.appbar.place()

    def hide(self):
        self.appbar.place_forget()
