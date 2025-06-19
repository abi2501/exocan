from PyQt6.QtWidgets import QMainWindow, QDockWidget, QTextEdit, QApplication
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resizable QDockWidget")
        self.setGeometry(100, 100, 600, 400)

        # Main editor
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        # Create dock widget
        self.dock = QDockWidget("Resizable Dock", self)
        self.dock.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        self.dock.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetMovable |
            QDockWidget.DockWidgetFeature.DockWidgetFloatable |
            QDockWidget.DockWidgetFeature.DockWidgetClosable
        )
        self.dock.setFloating(True)  # Let it float (undocked)

        # Set minimum/maximum size for resizing
        self.dock.setMinimumSize(200, 150)
        self.dock.setMaximumSize(800, 600)

        # Add content inside dock
        self.dock.setWidget(QTextEdit("Dock Content"))

        # Add to main window
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

