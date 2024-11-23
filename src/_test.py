import tkinter
import platform
from ui import widget
from ui.last_screen import end_screen, ask_screen, electric_screen
from util import theme, screen, controller, navigator


class TestScreen(screen.Screen): # 가전
    def __init__(self, root):
        self.root = root
        self.appbar = widget.AppBar(root, title="테스트 스크린", action=None)

        self.scroll_canvas = tkinter.Canvas(root, background=theme.color_background, highlightthickness=0)
        self.scroll_bar = tkinter.Scrollbar(root, orient=tkinter.VERTICAL, command=self.scroll_canvas.yview)
        self.scroll_frame = tkinter.Frame(self.scroll_canvas, background=theme.color_background)
        self.scroll_canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_canvas.bind("<Configure>", lambda event: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))
        self.scroll_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        self.na = [navigator.GoPage.DEFAULT, navigator.GoPage.FOOD, navigator.GoPage.NUCLEARSEED, navigator.GoPage.PINE, navigator.GoPage.BONE, navigator.GoPage.ROOT, navigator.GoPage.PAPER, navigator.GoPage.GLASS, navigator.GoPage.METAL, navigator.GoPage.BATTERY, navigator.GoPage.LIGHT, navigator.GoPage.APPLIANCE, navigator.GoPage.PHONE, navigator.GoPage.GOMPANGI]
        self.na2 = ["navigator.GoPage.DEFAULT", "navigator.GoPage.FOOD", "navigator.GoPage.NUCLEARSEED", "navigator.GoPage.PINE", "navigator.GoPage.BONE", "navigator.GoPage.ROOT", "navigator.GoPage.PAPER", "navigator.GoPage.GLASS", "navigator.GoPage.METAL", "navigator.GoPage.BATTERY", "navigator.GoPage.LIGHT", "navigator.GoPage.APPLIANCE", "navigator.GoPage.PHONE", "navigator.GoPage.GOMPANGI"]
        self.buttons = []
        for i in range(len(self.na)):
            self.buttons.append(
                widget.MyButton(
                    self.scroll_frame,
                    text=self.na2[i],
                    background=theme.color_button1,
                    foreground=theme.color_on_button1,
                    on_click=lambda i_=i: self.na[i_](root, "")
                )
            )
        self.total_height = 120 * len(self.na) + 40 * (len(self.na) + 1)

        self.scroll_frame.configure(height=self.total_height, width=720-30)
        if platform.system() == "Windows":  # Windows 일 때
            self.scroll_frame.bind_all(
                "<MouseWheel>",
                lambda event: self.scroll_canvas.yview_scroll(-1 * event.delta // 120, "units")
            )
        else:  # macOS 일 떄
            self.scroll_frame.bind_all(
                "<MouseWheel>",
                lambda event: self.scroll_canvas.yview_scroll(-1 * event.delta, "units")
            )


    def show(self):
        self.appbar.place()

        self.scroll_canvas.place(
            x=0, y=120,
            width=720-30, height=1080-120
        )
        self.scroll_bar.place(
            x=720-30, y=120,
            width=30, height=1080-120
        )
        for i in range(0, len(self.buttons)):
            self.buttons[i].place(
                x=40, y=40+(120+40)*i,
                width=720-40*2-30, height=120
            )


    def hide(self):
        self.appbar.place_forget()

        self.scroll_canvas.place_forget()
        self.scroll_bar.place_forget()
        for button in self.buttons:
            button.place_forget()


test_window = tkinter.Tk()

test_window.geometry("720x1080")
test_window.title("테스트 윈도우")
test_window.resizable(False, False)
test_window.config(background=theme.color_background)
controller.init(test_window)
controller.change_screen(TestScreen(test_window))

test_window.mainloop()
