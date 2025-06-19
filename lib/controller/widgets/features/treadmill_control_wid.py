from PyQt6.QtWidgets import QWidget

from lib.controller.views.components.tread_ctl_ui import Ui_Form


class TreadmillControlUI(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

