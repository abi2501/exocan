from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDockWidget, QWidget,
    QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QTextEdit
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


class VerticalAccordionDock(QDockWidget):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setAllowedAreas(Qt.DockWidgetArea.TopDockWidgetArea | Qt.DockWidgetArea.BottomDockWidgetArea)
        self.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)

        self.original_height = 200
        self.collapsed = False

        # Main dock widget content
        self.content = QLabel("Dock Content Here")
        content_wrapper = QWidget()
        content_layout = QVBoxLayout(content_wrapper)
        content_layout.setContentsMargins(5, 5, 5, 5)
        content_layout.addWidget(self.content)
        self.setWidget(content_wrapper)

        # Custom title bar
        self.setTitleBarWidget(self.create_title_bar())

    def create_title_bar(self):
        bar = QWidget()
        layout = QHBoxLayout(bar)
        layout.setContentsMargins(5, 2, 5, 2)

        title = QLabel(self.windowTitle())
        layout.addWidget(title)

        layout.addStretch()

        self.arrow_btn = QPushButton()
        self.arrow_btn.setIcon(QIcon.fromTheme("arrow-up"))  # Use your own icons
        self.arrow_btn.setFixedSize(20, 20)
        self.arrow_btn.setFlat(True)
        self.arrow_btn.clicked.connect(self.toggle_vertical_accordion)
        layout.addWidget(self.arrow_btn)

        return bar

    def toggle_vertical_accordion(self):
        if not self.collapsed:
            self.original_height = self.height()
            self.setMaximumHeight(30)
            self.arrow_btn.setIcon(QIcon.fromTheme("arrow-down"))  # Collapsed icon
            self.collapsed = True
        else:
            self.setMaximumHeight(16777215)
            self.resize(self.width(), self.original_height)
            self.arrow_btn.setIcon(QIcon.fromTheme("arrow-up"))  # Expanded icon
            self.collapsed = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Accordion DockWidget")
        self.resize(800, 600)

        # Central editor
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        # Top dock widget
        self.dock = VerticalAccordionDock("Console Panel", self)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.dock)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
