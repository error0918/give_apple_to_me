import tkinter
import tkinter.font

test_window = tkinter.Tk()

test_window.geometry("480x480")
test_window.title("TEST")

msg = tkinter.Message(test_window, text=str(tkinter.font.names()), relief="solid", background="white")
msg.pack()

test_window.mainloop()
