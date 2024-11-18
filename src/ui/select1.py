import tkinter
from . import controller
from . import navigator
from . import screen
from . import theme
from . import widget
from . import select2


class Select1(screen.Screen):
    def __init__(self, root):
        self.root = root
        self.appbar =  widget.AppBar(
            root=root,
            title="대분류 선택",
            action=lambda : controller.init(root)
        )
        self.buttons = []
        for division in navigator.Division:
            self.buttons.append(
                tkinter.Button(
                    root,
                    text = division.value,
                    padx=40, pady=20,
                    background=theme.color_background,
                    fg=theme.color_on_background,
                    borderwidth=1,
                    font=theme.font(size=40),
                    command=lambda root_=self.root, division_=division: controller.change_screen(select2.Select2(root=root_, division=division_))
                )
            )

    def show(self):
        self.appbar.place()
        for i in range(0, len(self.buttons)):
            self.buttons[i].place(
                x=40, y=120+40+(120+40)*i,
                width=640, height=120
            )

    def hide(self):
        self.appbar.place_forget()
        for button in self.buttons:
            button.place_forget()
