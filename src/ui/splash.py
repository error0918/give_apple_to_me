import tkinter
from . import controller
from . import screen
from . import theme
from . import select1


class Splash(screen.Screen):
    def __init__(self, root):
        self.root = root
        self.title = tkinter.Label(
            root,
            text = "사과해요나한테",
            background=theme.color_primary,
            fg=theme.color_on_content,
            font=theme.font(size=80, bold=True)
        )
        self.start_button = tkinter.Button(
            root,
            text = "시작하기",
            padx=40, pady=20,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=1,
            font=theme.font(size=40),
            command=lambda : controller.change_screen(select1.Select1(root))
        )
        self.description = tkinter.Label(
            root,
            text = "사과해요나한테, 성균관대학교, 2024",
            background=theme.color_primary,
            fg=theme.color_on_content,
            font=theme.font(size=15)
        )
        self.deco1 = tkinter.Canvas(root, bg=theme.color_primary, highlightthickness=0)
        self.deco1.create_oval(-360, -360, 360, 360, outline=theme.color_secondary, fill=theme.color_secondary)
        self.deco2 = tkinter.Canvas(root, bg=theme.color_primary, highlightthickness=0)
        self.deco2.create_oval(0, 0, 180, 180, outline=theme.color_secondary, fill=theme.color_secondary)


    def show(self):
        self.root.configure(background=theme.color_primary)
        self.title.place(x=0, y=540-100, width=720, height=200)
        self.start_button.place(x=360-120, y=700, width=240, height=120)
        self.description.place(x=360-120, y=1040, width=240, height=30)
        self.deco1.place(x=0, y=0, width=360, height=360)
        self.deco2.place(x=530, y=240, width=180, height=180)


    def hide(self):
        self.root.configure(background=theme.color_background)
        self.title.place_forget()
        self.start_button.place_forget()
        self.description.place_forget()
        self.deco1.place_forget()
        self.deco2.place_forget()
