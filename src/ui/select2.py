import tkinter
from . import controller
from . import screen
from . import select1
from . import theme


class Select2AppBar:
    def __init__(self, root, title):
        self.root = root
        self.appbar = tkinter.Label(
            root,
            text = title,
            background=theme.color_primary,
            fg=theme.color_on_content,
            font=theme.font(size=50, bold=True)
        )
        self.appbar_button = tkinter.Label(
            root,
            text = "<",
            cursor="hand2",
            background=theme.color_primary,
            fg=theme.color_on_content,
            font=theme.font(size=60, bold=True)
        ) # 투명하게 하기 위해 가짜 버튼
        self.appbar_button.bind("<Button-1>", lambda event: controller.change_screen(select1.Select1(root)))

    def place(self):
        self.appbar.place(x=0, y=0, width=720, height=120)
        self.appbar_button.place(x=0, y=0, width=120, height=120)

    def place_forget(self):
        self.appbar.place_forget()


class Select2a(screen.Screen):
    def __init__(self, root):
        self.root = root
        self.appbar = Select2AppBar(root, "가전")

    def show(self):
        self.appbar.place()

    def hide(self):
        self.appbar.place_forget()


class Select2b(screen.Screen):
    def __init__(self, root):
        self.root = root
        self.appbar = Select2AppBar(root, "음식물")

    def show(self):
        self.appbar.place()

    def hide(self):
        self.appbar.place_forget()


class Select2c(screen.Screen):
    def __init__(self, root):
        self.root = root
        self.appbar = Select2AppBar(root, "생활 쓰레기")

    def show(self):
        self.appbar.place()

    def hide(self):
        self.appbar.place_forget()


class Select2d(screen.Screen):
    def __init__(self, root):
        self.root = root
        self.appbar = Select2AppBar(root, "기타")

    def show(self):
        self.appbar.place()

    def hide(self):
        self.appbar.place_forget()
