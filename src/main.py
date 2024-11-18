import tkinter
import pyglet
from ui import theme
from ui import controller


main_window = tkinter.Tk()

main_window.geometry("720x1080")
main_window.title("사과해요나한테")
main_window.resizable(False, False)
main_window.config(background=theme.color_background)
pyglet.font.add_file("res/NanumSquareNeo_Regular.ttf")
pyglet.font.add_file("res/NanumSquareNeo_Bold.ttf")
controller.init(main_window)

main_window.mainloop()
