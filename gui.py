import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlFile
from pyforms.Controls import ControlLabel


class ResultWindow(BaseWidget):
    def __init__(self):
        BaseWidget.__init__(self,'ResultWindow')
        self._test = ControlLabel("result")

class Menu(BaseWidget):
    def __init__(self):
        super(Menu, self).__init__('Simple example 1')

        # Definition of the forms fields
        self._input = ControlFile()
        self._test = ControlButton('Start')
        self._test.valie = self.__buttonAction()

    def __buttonAction(self):
        win = ResultWindow()
        win.parent = self
        win.show()

# Execute the application
if __name__ == "__main__":   pyforms.startApp(Menu)
