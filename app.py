import sys

from PyQt6.QtWidgets import QApplication
import res
from lib.controller.app_screen import MainWindow
from PyQt6.QtGui import QFont, QFontDatabase

from lib.controller.util.helper import resource_path

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Load the Poppins font
    font_id = QFontDatabase.addApplicationFont(resource_path("lib/assets/fonts/Poppins/Poppins-Regular.ttf"))
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        app.setFont(QFont(font_family))
    else:
        print("Failed to load Poppins font.")

    main_window = MainWindow()

    # main_window.show()
    main_window.showMaximized()

    sys.exit(app.exec())