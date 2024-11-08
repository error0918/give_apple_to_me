from . import screen
from . import splash


now = splash.Splash()


def init():
    now.show()

def change_screen(new: screen.Screen):
    global now
    now.hide()
    now = new
    now.show()
