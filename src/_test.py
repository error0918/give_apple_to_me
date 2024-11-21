import tkinter
from ui import widget
from ui.last_screen import end_screen, ask_screen, electric_screen
from util import theme, screen, controller


class TestScreen(screen.Screen): # 가전
    def __init__(self, root):
        self.root = root
        self.appbar = widget.AppBar(root, title="테스트 스크린", action=None)
        self.button1 = widget.MyButton(
            root,
            on_click=self.button1,
            text="버튼 1",
            subtext="TODO"
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
        controller.change_screen(
            electric_screen.ElectricScreen(
                self.root,
                depot_type=electric_screen.DepotType.PHONE
            )
        )

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
        def text_edit(text: tkinter.Text):
            text.tag_configure(
                tagName="highlight",
                foreground=theme.color_point,
                font=theme.font(size=35, bold=True)
            )
            # self.a = tkinter.PhotoImage(file="res/test.png").subsample(3, 3)
            # text.image_create("1.0", image=self.a)
            # text.insert(tkinter.END, "\n\n")
            text.insert(tkinter.END, "음식물 쓰레기는 자연의 순환을 위한 소중한 자원입니다.\n\n")
            text.insert(tkinter.END, "물기를 최대한 제거하고, 이물질을 골라낸 후 음식물 쓰레기 전용 봉투에 담아 지정된 장소에 배출해 주세요. ", "highlight")
            text.insert(tkinter.END, "올바른 분리배출이 지구를 건강하게 만듭니다.")
        controller.change_screen(
            end_screen.EndScreen(
                self.root,
                title="음식물 쓰레기",
                content=None,
                text_edit=text_edit
            )
        )

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
controller.init(test_window)
controller.change_screen(TestScreen(test_window))

test_window.mainloop()
