import tkinter
from ui import screen
from ui import widget
from ui import theme


class EndScreen(screen.Screen): # 생활 쓰레기
    def __init__(self, root, title: str, content: str):
        self.root = root
        self.appbar = widget.AppBar(
            root=root,
            title=title,
            action=None
        )
        self.content_label = tkinter.Text(
            root,
            background=theme.color_background,
            fg=theme.color_on_background,
            wrap="word",
            borderwidth=0,
            highlightthickness=0,
            font=theme.font(size=25)
        )
        self.content_label.insert("1.0", content)
        self.restart_bar = widget.RestartBar(root)

    def show(self):
        self.appbar.place()
        self.content_label.place(x=20, y=120+20, width=720-20*2, height=1080-120*2-20*2)
        self.restart_bar.place()

    def hide(self):
        self.appbar.place_forget()
        self.content_label.place_forget()
        self.restart_bar.place_forget()