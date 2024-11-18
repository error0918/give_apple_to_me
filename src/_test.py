import tkinter
import pyglet
import platform
from enum import Enum
from dataclasses import dataclass
from ui import theme
from ui import controller
from ui import screen
from ui import widget
from ui.subpage import end_screen


print(platform.system())

"""
# 쓰레기 대분류
class Division(Enum):
    ELECTRIC = "전자제품"
    FOOD = "음식물"
    LIVING = "생활 쓰레기"
    ETC = "기타"


# 연결 페이지
class GoPage(Enum):
    DEFAULT = lambda root, name: navigator.nav_default(root=root, name=name)  # 일반 쓰레기
    FOOD = lambda root, name: navigator.nav_food(root=root, name=name)  # 음식물 쓰레기
    PAPER = lambda root, name: navigator.nav_paper(root=root, name=name)  # 종이류
    GLASS = lambda root, name: navigator.nav_glass(root=root, name=name)  # 유리류
    METAL = lambda root, name: navigator.nav_metal(root=root, name=name)  # 금속류
    PLASTIC = lambda root, name: navigator.nav_plastic(root=root, name=name)  # 플라스틱
    BATTERY = lambda root, name: navigator.nav_battery(root=root, name=name)  # 전지류
    LIGHT = lambda root, name: navigator.nav_light(root=root, name=name)  # 형광등
    CLOTH = lambda root, name: navigator.nav_cloth(root=root, name=name)  # 의류
    SMALL_APPLIANCE = lambda root, name: navigator.nav_small_appliance(root=root, name=name)  # 소형 폐가전
    BIG_APPLIANCE = lambda root, name: navigator.nav_big_appliance(root=root, name=name)  # 대형 폐가전
    GOMPANGI = lambda root, name: navigator.nav_gompangi(root=root, name=name)  # 곰팡이가 피었나요?


@dataclass(frozen=True)
class TrashItem:
    name: str  # 쓰레기 이름
    search_keywords: list[str]  # 검색 키워드
    divisions: list[Division]  # 대분류
    go_page: GoPage  # 연결 페이지


dataset = [
    TrashItem(
        name = "사과",
        search_keywords=["ㅅ", "사", "삭", "사고", "사과"] + ["ㅅ", "ㅅㄱ"],
        divisions=[Division.FOOD],
        go_page=GoPage.GOMPANGI
    )
]


class TestScreen(screen.Screen): # 가전
    def __init__(self, root):
        self.root = root
        self.appbar = widget.AppBar(root, title="테스트 스크린", action=None)
        self.button1 = tkinter.Button(
            root,
            text = "버튼 1",
            padx=40, pady=20,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=1,
            font=theme.font(size=40),
            command=self.button1
        )
        self.button2 = tkinter.Button(
            root,
            text = "버튼 2",
            padx=40, pady=20,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=1,
            font=theme.font(size=40),
            command=self.button2
        )

    def button1(self):
        controller.change_screen(end_screen.EndScreen(self.root, title="테스트 엔드 스크린", content="테스트 엔드 스크린 내용 입니다. " * 100))

    def button2(self):
        pass

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

    def hide(self):
        self.appbar.place_forget()
        self.button1.place_forget()
        self.button2.place_forget()


test_window = tkinter.Tk()

test_window.geometry("720x1080")
test_window.title("테스트 윈도우")
test_window.resizable(False, False)
test_window.config(background=theme.color_background)
pyglet.font.add_file("res/NanumSquareNeo.ttf")
controller.init(test_window)
controller.change_screen(TestScreen(test_window))

test_window.mainloop()
"""
