import tkinter
from typing import Callable, Optional
from ui import widget
from util import theme, screen


class EndScreen(screen.Screen): # 생활 쓰레기
    def __init__(
            self, root,
            title: str,
            content: Optional[str],
            text_edit: Optional[Callable[[tkinter.Text], None]]=None
    ):
        self.root = root
        self.appbar = widget.AppBar(
            root=root,
            title=title,
            action=None
        )
        self.content_text = tkinter.Text(
            root,
            background=theme.color_background,
            fg=theme.color_on_background,
            wrap="word",
            borderwidth=0,
            highlightthickness=0,
            font=theme.font(size=35)
        )
        self.content_text.tag_configure("left", justify='left')
        self.content_text.tag_configure("center", justify='center')
        self.content_text.tag_configure("right", justify='right')
        self.content_text.tag_configure("line_spacing", spacing2=15)
        if content:
            self.content_text.insert("1.0", content)
        if text_edit:
            text_edit(self.content_text)
        self.content_text.tag_add("line_spacing", "1.0", "end")
        self.content_text.configure(state=tkinter.DISABLED)

        self.restart_bar = widget.RestartBar(root)


    def show(self):
        self.appbar.place()
        self.content_text.place(
            x=20, y=120 + 20,
            width=720 - 20 * 2, height=1080 - 120 * 2 - 20 * 2
        )
        self.restart_bar.place()


    def hide(self):
        self.appbar.place_forget()
        self.content_text.place_forget()
        self.restart_bar.place_forget()