from typing import Optional
from . import screen
from . import select2
from . import splash


dataset = {
    "가전": lambda root: select2.Select2a(root),
    "음식물": lambda root: select2.Select2b(root),
    "생활 쓰레기": lambda root: select2.Select2c(root),
    "기타": lambda root: select2.Select2d(root)
}

now: Optional[screen.Screen] = None


def init(root):
    global now
    if now is not None:
        now.hide()
    now = splash.Splash(root)
    now.show()

def change_screen(new: screen.Screen):
    global now
    now.hide()
    now = new
    now.show()
