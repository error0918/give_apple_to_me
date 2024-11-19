import tkinter
import platform
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
        self.search_bar = tkinter.Frame(root, background=theme.color_secondary)
        self.search_variable = tkinter.StringVar()
        self.search_entry = tkinter.Entry(
            self.search_bar,
            background=theme.color_secondary,
            foreground=theme.color_on_content,
            borderwidth=1,
            highlightthickness=0,
            font=theme.font(30),
            justify="left",
            relief="flat",
            textvariable=self.search_variable
        )
        self.search_hint = tkinter.Label(
            self.search_bar,
            text="검색할 키워드를 입력하세요..",
            cursor="hand2",
            background=theme.color_secondary,
            foreground=theme.color_hint,
            font=theme.font(size=30, italic=True),
            anchor="w"
        )
        self.search_clear = tkinter.Label(
            self.search_bar,
            text = "X",
            cursor="hand2",
            background=theme.color_secondary,
            fg=theme.color_on_content,
            font=theme.font(size=60, bold=True)
        ) # 투명하게 하기 위해 가짜 버튼
        self.search_clear.bind("<Button-1>", lambda event: self.search_entry.delete(0, tkinter.END))

        self.search_variable.trace("w", self.on_text_changed)
        def show_hint(__event):
            if self.search_entry.get().strip() == "":
                self.search_hint.place(
                    x=40, y=20,
                    width=720-40*2, height=80
                )
        self.search_entry.bind("<FocusIn>", lambda event: self.search_hint.place_forget())
        self.search_entry.bind("<FocusOut>", show_hint)
        self.search_hint.bind("<Button-1>", lambda event: self.search_entry.focus_set())

        self.scroll_canvas = tkinter.Canvas(root, background=theme.color_background, highlightthickness=0)
        self.scroll_bar = tkinter.Scrollbar(root, orient=tkinter.VERTICAL, command=self.scroll_canvas.yview)
        self.scroll_frame = tkinter.Frame(self.scroll_canvas, background=theme.color_background)
        self.scroll_canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_canvas.bind("<Configure>", lambda event: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))
        self.scroll_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        self.buttons = []
        for division in navigator.Division:
            self.buttons.append(
                widget.MyButton(
                    self.scroll_frame,
                    text=division.value,
                    subtext="대분류",
                    background=theme.color_button1,
                    foreground=theme.color_on_button1,
                    on_click=lambda root_=self.root, division_=division: controller.change_screen(select2.Select2(root=root_, division=division_))
                )
            )
        self.total_height = 120 * len(navigator.Division) + 40 * (len(navigator.Division) + 1)

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


    def on_text_changed(self, *args):
        value = self.search_variable.get().strip()
        if value == "":
            # SearchBar 수정
            self.search_clear.place_forget()
            self.search_entry.place(
                x=40, y=20,
                width=720-40*2, height=80
            )

            # 버튼 수정
            self.hide_buttons()
            self.buttons = []
            for division in navigator.Division:
                self.buttons.append(
                    widget.MyButton(
                        self.scroll_frame,
                        text=division.value,
                        subtext="대분류",
                        background=theme.color_button1,
                        foreground=theme.color_on_button1,
                        on_click=lambda root_=self.root, division_=division: controller.change_screen(select2.Select2(root=root_, division=division_))
                    )
                )

            self.total_height = 120 * len(navigator.Division) + 40 * (len(navigator.Division) + 1)
            self.scroll_frame.configure(height=self.total_height, width=720-30)
            self.show_buttons()
        else:
            # SearchBar 수정
            self.search_clear.place(
                x=720-40-80, y=20,
                width=80, height=80
            )
            self.search_entry.place(
                x=40, y=20,
                width=720-40*2-20-80, height=80
            )

            # 버튼 수정
            self.hide_buttons()
            filtered_items = list(sorted(filter(lambda x: value in x.search_keywords, navigator.dataset), key=lambda x: x.name))
            self.buttons = []
            for item in filtered_items:
                self.buttons.append(
                    widget.MyButton(
                        self.scroll_frame,
                        text = item.name,
                        background=theme.color_button2,
                        foreground=theme.color_on_button2,
                        on_click=lambda function=item.go_page, name=item.name: function(self.root, name)
                    )
                )

            self.total_height = 120 * len(filtered_items) + 40 * (len(filtered_items) + 1)
            self.scroll_frame.configure(height=self.total_height, width=720-30)
            self.show_buttons()


    def show_buttons(self):
        if self.total_height > 1080 - 120 * 2: # 스크롤바가 있을 때
            self.scroll_canvas.place(
                x=0, y=120*2,
                width=720-30, height=1080-120*2
            )
            self.scroll_bar.place(
                x=720-30, y=120*2,
                width=30, height=1080-120*2
            )
            for i in range(0, len(self.buttons)):
                self.buttons[i].place(
                    x=40, y=40+(120+40)*i,
                    width=720-40*2-30, height=120
                )
        else:
            for i in range(0, len(self.buttons)):
                self.scroll_canvas.place(
                    x=0, y=120*2,
                    width=720, height=1080-120*2
                )
                self.buttons[i].place(
                    x=40, y=40+(120+40)*i,
                    width=720-40*2, height=120
                )


    def hide_buttons(self):
        self.scroll_canvas.place_forget()
        self.scroll_bar.place_forget()
        for button in self.buttons:
            button.place_forget()


    def show(self):
        self.appbar.place()
        self.search_bar.place(
            x=0, y=120,
            width=720, height=120
        )
        self.search_entry.place(
            x=40, y=20,
            width=720-40*2, height=80
        )
        self.search_hint.place(
            x=40, y=20,
            width=720-40*2, height=80
        )
        self.show_buttons()
        self.search_bar.focus_set()


    def hide(self):
        self.appbar.place_forget()
        self.search_bar.place_forget()
        self.hide_buttons()
