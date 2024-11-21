import platform
import tkinter.font


# 색상
color_background = "#FFFFFF"
color_on_background = "#000000"

color_toast = "#444444"
color_on_toast = "#FFFFFF"

color_primary = "#4BC687"
color_secondary = "#79CBA0"
color_on_content = "#FFFFFF"
color_hint = "#DDDDDD"
color_point = "#990D19"  # Easter Egg: Boogie Man Red
color_sub = "#AAAAAA"

color_container = "#19814B"
color_on_container = "#FFFFFF"
color_button1 = "#EEEEEE"
color_on_button1 = "#000000"
color_button2 = "#FFFFFF"
color_on_button2 = "#000000"


# 폰트
def font(
        size: int = 20,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        overstrike: bool = False
):
    if platform.system() == "Windows":
        size = int(size * 0.8)
    return tkinter.font.Font(
        family="Arial",
        size=size,
        weight="bold" if bold else "normal",
        slant="italic" if italic else "roman",
        underline=underline,
        overstrike=overstrike,
    )
