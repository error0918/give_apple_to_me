import tkinter
from typing import Callable, Optional
from ui import widget
from util import theme, screen


class AskScreen(screen.Screen): # 음식물
    def __init__(
            self, root,
            title: str,
            content: Optional[str],
            command_no: Callable[[], None],
            command_yes: Callable[[], None],
            command_back: Optional[Callable[[], None]] = None,
            text_no: str = "아니요",
            text_yes: str = "예",
            centered: bool=True,
            text_edit: Optional[Callable[[tkinter.Text], None]]=None
    ):
        self.root = root
        self.appbar = widget.AppBar(
            root=root,
            title=title,
            action=command_back
        )

        self.content_text = tkinter.Text(
            root,
            background=theme.color_background,
            fg=theme.color_on_background,
            wrap="word",
            borderwidth=0,
            highlightthickness=0,
            font=theme.font(size=45 if centered else 35, bold=True)
        )
        self.content_text.tag_configure("left", justify='left')
        self.content_text.tag_configure("center", justify='center')
        self.content_text.tag_configure("right", justify='right')
        if content:
            if centered:
                self.content_text.insert(
                    "1.0",
                    "\n" * (280 // int(45 * 0.8) - len(content) // 45)
                )
                self.content_text.insert(tkinter.END, content, "center")
            else:
                self.content_text.tag_configure("line_spacing", spacing2=15)
                self.content_text.insert(tkinter.END, content)
                self.content_text.tag_add("line_spacing", "1.0", "end")
            self.content_text.configure(state=tkinter.DISABLED)
        if text_edit:
            text_edit(self.content_text)

        self.no_button = widget.MyButton(
            self.root,
            on_click=command_no,
            text=text_no,
            background=theme.color_container,
            foreground=theme.color_on_container,
            has_border=False
        )
        self.yes_button = widget.MyButton(
            self.root,
            on_click=command_yes,
            text=text_yes,
            background=theme.color_container,
            foreground=theme.color_on_container,
            has_border=False
        )
        self.button_border = tkinter.Frame(
            self.root,
            background=theme.color_on_container,
            borderwidth=0,
            highlightthickness=0
        )


    def show(self):
        self.appbar.place()
        self.content_text.place(
            x=20, y=120 + 20,
            width=720 - 20 * 2, height=1080 - 120 * 2 - 20 * 2
        )
        self.no_button.place(
            x=0, y=1080-120,
            width=360, height=120
        )
        self.yes_button.place(
            x=360, y=1080-120,
            width=360, height=120
        )
        self.button_border.place(
            x=360, y=1080-120,
            width=1, height=120
        )


    def hide(self):
        self.appbar.place_forget()
        self.content_text.place_forget()
        self.no_button.place_forget()
        self.yes_button.place_forget()
        self.button_border.place_forget()
