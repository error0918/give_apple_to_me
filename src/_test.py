import tkinter
import pyglet
import platform
from enum import Enum
from dataclasses import dataclass
from ui import widget
from ui.last_screen import end_screen
from util import theme, screen, controller




"""
class TestScreen(screen.Screen): # 가전
    def __init__(self, root):
        self.root = root
        self.appbar = widget.AppBar(root, title="테스트 스크린", action=None)
        self.button1 = tkinter.Button(
            root,
            text = "버튼 1",
            padx=40, pady=20,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=1,
            font=theme.font(size=40),
            command=self.button1
        )
        self.button2 = tkinter.Button(
            root,
            text = "버튼 2",
            padx=40, pady=20,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=1,
            font=theme.font(size=40),
            command=self.button2
        )

    def button1(self):
        controller.change_screen(end_screen.EndScreen(self.root, title="테스트 엔드 스크린", content="테스트 엔드 스크린 내용 입니다. " * 100))

    def button2(self):
        pass

    def show(self):
        self.appbar.place()
        self.button1.place(
            x=40, y=120+40,
            width=640, height=120
        )
        self.button2.place(
            x=40, y=120+40+160,
            width=640, height=120
        )

    def hide(self):
        self.appbar.place_forget()
        self.button1.place_forget()
        self.button2.place_forget()


test_window = tkinter.Tk()

test_window.geometry("720x1080")
test_window.title("테스트 윈도우")
test_window.resizable(False, False)
test_window.config(background=theme.color_background)
pyglet.font.add_file("res/NanumSquareNeo.ttf")
controller.init(test_window)
controller.change_screen(TestScreen(test_window))

test_window.mainloop()
"""