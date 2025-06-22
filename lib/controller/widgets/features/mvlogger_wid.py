from PyQt6.QtWidgets import QWidget, QVBoxLayout

from lib.controller.views.components.mvlogger_ui import Ui_Form
from resizer import AccordionDockWidget


class MvLoggerUI(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.accord_dock = AccordionDockWidget()
        self.accord_dock = AccordionDockWidget()

        vlayout = QVBoxLayout()
        self.ui.logger_widget.setLayout(vlayout)
        vlayout.addWidget(self.accord_dock)