from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QCheckBox, QTextEdit, QFrame
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


class AccordionSection(QFrame):
    def __init__(self, title, content: QWidget, parent=None):
        super().__init__(parent)
        self.setStyleSheet("QFrame { background-color: #2b2b2b; border-radius: 8px; }")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

        # Header
        header = QWidget()
        header.setStyleSheet("background-color: #333333; padding: 5px;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(10, 5, 10, 5)
        header_layout.setSpacing(5)

        icon_label = QLabel()
        icon_label.setPixmap(QIcon.fromTheme("applications-system").pixmap(QSize(16, 16)))
        header_layout.addWidget(icon_label)

        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("color: white; font-weight: bold;")
        header_layout.addWidget(self.title_label)

        header_layout.addStretch()

        self.toggle_button = QPushButton()
        self.toggle_button.setIcon(QIcon.fromTheme("arrow-down"))
        self.toggle_button.setFixedSize(24, 24)
        self.toggle_button.setFlat(True)
        self.toggle_button.clicked.connect(self.toggle_content)
        header_layout.addWidget(self.toggle_button)

        # Content
        self.content = content
        self.content.setVisible(True)

        self.layout().addWidget(header)
        self.layout().addWidget(self.content)

    def toggle_content(self):
        is_visible = self.content.isVisible()
        self.content.setVisible(not is_visible)
        self.toggle_button.setIcon(QIcon.fromTheme("arrow-up" if is_visible else "arrow-down"))


class LoggerPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # Toolbar Row
        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(0, 0, 0, 0)

        auto_scroll = QCheckBox("Auto-scroll")
        auto_scroll.setStyleSheet("color: white;")
        clear_button = QLabel('<a href="#">Clear</a>')
        clear_button.setStyleSheet("color: #00aaff;")
        clear_button.setOpenExternalLinks(False)

        toolbar_layout.addWidget(auto_scroll)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(clear_button)

        layout.addWidget(toolbar)

        # Log Box
        self.log_text = QTextEdit()
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #ffaa00;
                border: 1px solid #555;
                border-radius: 4px;
            }
        """)
        self.log_text.setPlainText("Trace1 Start")
        layout.addWidget(self.log_text)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Accordion Dock")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(8)

        logger_panel = AccordionSection("mvLogger", LoggerPanel())
        settings_panel = AccordionSection("Setting", QLabel("Settings content here..."))
        settings_panel.toggle_content()  # start collapsed

        main_layout.addWidget(logger_panel)
        main_layout.addWidget(settings_panel)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.resize(300, 400)
    window.setStyleSheet("QWidget { background-color: #1a1a1a; }")
    window.show()
    app.exec()
