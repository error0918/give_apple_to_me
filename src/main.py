import tkinter
from util import theme, controller

main_window = tkinter.Tk()

main_window.geometry("720x1080")
main_window.title("일반분리학")
main_window.resizable(False, False)
main_window.config(background=theme.color_background)
controller.init(main_window)

main_window.mainloop()
