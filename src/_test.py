import tkinter
import pyglet
from ui import widget
from ui.last_screen import end_screen, ask_screen
from util import theme, screen, controller


class TestScreen(screen.Screen): # 가전
    def __init__(self, root):
        self.root = root
        self.appbar = widget.AppBar(root, title="테스트 스크린", action=None)
        self.button1 = widget.MyButton(
            root,
            on_click=self.button1,
            text="버튼 1",
            subtext="엔드 스크린"
        )
        self.button2 = widget.MyButton(
            root,
            on_click=self.button2,
            text="버튼 2",
            subtext="애스크 스크린"
        )
        self.button3 = widget.MyButton(
            root,
            on_click=self.button3,
            text="버튼 3",
            subtext="문구 스크린"
        )

    def button1(self):
        controller.change_screen(end_screen.EndScreen(self.root, title="테스트 엔드 스크린", content="테스트 엔드 스크린 내용 입니다. " * 100))

    def button2(self):
        controller.change_screen(
            ask_screen.AskScreen(
                self.root,
                title="테스트 애스크 스크린",
                content="테스트 애스크 스크린 내용 입니다." * 5,
                command_no=lambda : print("TEST1"),
                command_yes=lambda : print("TEST1")
            )
        )

    def button3(self):
        controller.change_screen(
            None
        )  # TODO

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
        self.button3.place(
            x=40, y=(120+40)*2+160,
            width=640, height=120
        )

    def hide(self):
        self.appbar.place_forget()
        self.button1.place_forget()
        self.button2.place_forget()
        self.button3.place_forget()


test_window = tkinter.Tk()

test_window.geometry("720x1080")
test_window.title("테스트 윈도우")
test_window.resizable(False, False)
test_window.config(background=theme.color_background)
pyglet.font.add_file("res/NanumSquareNeo_Regular.ttf")
pyglet.font.add_file("res/NanumSquareNeo_Bold.ttf")
controller.init(test_window)
controller.change_screen(TestScreen(test_window))

test_window.mainloop()
