import pyglet
import tkinter.font


# 초기 설정
def init():
    pyglet.font.add_file("res/NanumSquareNeo.ttf")


# 색상
color_background = "#FFFFFF"
color_on_background = "#000000"

color_primary = "#4BC687"
color_secondary = "#62CC93"
color_on_content = "#FFFFFF"

color_container = "#B8E0D0"
color_on_container = "#000000"


# 폰트
def font(
        size: int = 20,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        overstrike: bool = False
):
    return tkinter.font.Font(
        family=pyglet.font.load("NanumSquare Neo variable").name,
        size=size,
        weight="bold" if bold else "normal",
        slant="italic" if italic else "roman",
        underline=underline,
        overstrike=overstrike,
    )
