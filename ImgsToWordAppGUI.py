from abc import ABCMeta, abstractmethod
from ImgsToWordAppCLI import ImgsToWordAppCLI


class ImgsToWordAppGUI(ImgsToWordAppCLI, metaclass=ABCMeta):

    def run(self):
        self.init_gui_form()
        self.run_gui_loop()

    @abstractmethod
    def init_gui_form(self):
        pass

    @abstractmethod
    def run_gui_loop(self):
        pass

    @abstractmethod
    def alert(self, msg, *args, **kwargs):
        pass
 

if __name__ == "__main__":
    app = ImgsToWordAppGUI()
    app.run()
