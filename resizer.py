from PyQt6.QtWidgets import QApplication, QFrame, QVBoxLayout, QSizeGrip
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor

class ResizableFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resizable Frame")
        self.setGeometry(300, 300, 300, 200)
        self.setFrameShape(QFrame.Shape.Box)
        self.setStyleSheet("background-color: lightblue;")

        # Set the resize cursor
        self.setCursor(QCursor(Qt.CursorShape.SizeFDiagCursor))

        layout = QVBoxLayout(self)
        layout.addStretch()

        # Add QSizeGrip to bottom-right
        grip = QSizeGrip(self)
        layout.addWidget(grip, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

app = QApplication([])
frame = ResizableFrame()
frame.show()
app.exec()
