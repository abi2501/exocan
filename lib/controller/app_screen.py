import os

import qdarktheme
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout

from lib.controller.util.helper import resource_path
from lib.controller.views.main_screen import Ui_MainWindow
from lib.controller.widgets.features.exomusle_control_wid import ExoMuscleControlUI
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

        self.container_layout = QHBoxLayout()
        self.reziable_layout = QVBoxLayout()

        # self.set_main_control_layout()
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

        self.ui.frame.setLayout(self.container_layout)
        self.container_layout.addWidget(self.treadmill_ctl_wid)
        self.container_layout.addWidget(self.exo_muscle_ctl_wid)

        # # self.ui.main_wid
        # self.container_layout.addWidget(self.treadmill_ctl_wid)
        # self.container_layout.addWidget(self.exo_muscle_ctl_wid)
        # self.ui.main_wid.setLayout(self.container_layout)

        # self.ui.bottom_wid.setLayout(self.reziable_layout)

        # self.reziable_layout.addWidget(ResizableFrame())

    def set_slots(self):

        # Set Shortcut for close window on ctrl + c
        self.short_cut = QShortcut(QKeySequence("Ctrl+C"), self)
        self.short_cut.activated.connect(self.close)
