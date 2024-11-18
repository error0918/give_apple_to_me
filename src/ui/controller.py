from typing import Optional
from . import screen
from . import splash


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
