from tkinter import *
from ImgsToWordAppGUI import ImgsToWordAppGUI


class ImgsToWordAppGUI_TKI(ImgsToWordAppGUI):

    def run(self):
        self.init_gui_form()
        self.run_gui_loop()

    def init_gui_form(self):
        self.root = Tk()  # create root window
        self.root.title("Frame Example")
        self.root.config(bg="skyblue")

    def run_gui_loop(self):
        self.root.mainloop()

    def alert(self, msg, *args, **kwargs):
        pass
 

if __name__ == "__main__":
    app = ImgsToWordAppGUI_TKI()
    app.run()
