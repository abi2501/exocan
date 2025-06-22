import os

import qdarktheme
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout

from lib.controller.util.helper import resource_path
from lib.controller.views.main_screen import Ui_MainWindow
from lib.controller.widgets.features.exomusle_control_wid import ExoMuscleControlUI
from lib.controller.widgets.features.mvlogger_wid import MvLoggerUI
from lib.controller.widgets.features.treadmill_control_wid import TreadmillControlUI
# from resizer import ResizableFrame


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """ Instantiate Component Widgets """
        self.treadmill_ctl_wid = TreadmillControlUI()
        self.exo_muscle_ctl_wid = ExoMuscleControlUI()
        self.mv_logger_wid = MvLoggerUI()

        self.container_layout = QHBoxLayout()
        self.reziable_layout = QVBoxLayout()

        self.set_main_control_layout()
        self.init_settings()
        self.set_slots()

    def init_settings(self):
        """
            Initial configurations and settings
            Dark theme and exclusive CSS styling
         """
        qdarktheme.setup_theme("dark")

        styleFile = os.path.join(os.path.split(__file__)[0], resource_path("lib/assets/styles/style.qss"))

        with open(styleFile, 'r') as f:
            style = f.read()

        self.setStyleSheet(style)

    def set_main_control_layout(self):
        self.ui.ctrl_wid.layout().addWidget(self.treadmill_ctl_wid)
        self.ui.ctrl_wid.layout().addWidget(self.exo_muscle_ctl_wid)
        self.ui.ctrl_wid.layout().addWidget(self.mv_logger_wid)

        self.ui.ctrl_layout.setStretch(0,4)
        self.ui.ctrl_layout.setStretch(1,4)
        self.ui.ctrl_layout.setStretch(2,2)

    def set_slots(self):
        # Set Shortcut for close window on ctrl + c
        self.short_cut = QShortcut(QKeySequence("Ctrl+C"), self)
        self.short_cut.activated.connect(self.close)
