import tkinter
import platform
from . import controller
from . import navigator
from . import screen
from . import select1
from . import theme
from . import widget


class Select2(screen.Screen): # 가전
    def __init__(self, root, division: navigator.Division):
        self.root = root
        self.appbar = widget.AppBar(
            root=root,
            title=f"대분류: {division.value}",
            action=lambda : controller.change_screen(select1.Select1(root))
        )

        self.scroll_canvas = tkinter.Canvas(root, background=theme.color_background, highlightthickness=0)
        self.scroll_bar = tkinter.Scrollbar(root, orient=tkinter.VERTICAL, command=self.scroll_canvas.yview)
        self.scroll_frame = tkinter.Frame(self.scroll_canvas, background=theme.color_background)
        self.scroll_canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_canvas.bind("<Configure>", lambda event: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))
        self.scroll_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        self.filtered_items = list(sorted(filter(lambda x: division in x.divisions, navigator.dataset), key=lambda x: x.name))
        self.buttons = []
        for item in self.filtered_items:
            self.buttons.append(
                tkinter.Button(
                    self.scroll_frame,
                    text = item.name,
                    padx=40, pady=20,
                    background=theme.color_background,
                    fg=theme.color_on_background,
                    borderwidth=1,
                    font=theme.font(size=40),
                    command=lambda function=item.go_page, name=item.name: function(root, name)
                )
            )

        self.total_height = 120 * len(self.filtered_items) + 40 * (len(self.filtered_items) + 1)

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

        if self.total_height > 1080 - 120: # 스크롤바가 있을 때
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
        else: # 스크롤바가 없을 때
            self.scroll_canvas.place(
                x=0, y=120,
                width=720, height=1080-120
            )

            for i in range(0, len(self.buttons)):
                self.buttons[i].place(
                    x=40, y=40+(120+40)*i,
                    width=720-40*2, height=120
                )



    def hide(self):
        self.appbar.place_forget()
        self.scroll_canvas.place_forget()
        self.scroll_bar.place_forget()
        for button in self.buttons:
            button.place_forget()
