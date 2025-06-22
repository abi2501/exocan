from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDockWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QToolButton, QLabel, QCheckBox, QPushButton, QTextEdit, QSizePolicy, QFrame
)
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QIcon
import sys

class AccordionSection(QWidget):
    toggled = pyqtSignal(bool)  # Signal emitted when section is toggled

    def __init__(self, title, icon=None, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Header
        self.header = QFrame()
        self.header.setObjectName("AccordionHeader")
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(12, 4, 12, 4)
        self.header_layout.setSpacing(8)

        if icon:
            self.icon_label = QLabel()
            self.icon_label.setPixmap(QIcon(icon).pixmap(18, 18))
            self.header_layout.addWidget(self.icon_label)

        self.title_label = QLabel(title)
        self.header_layout.addWidget(self.title_label)

        self.header_layout.addStretch()

        self.arrow_btn = QToolButton()
        self.arrow_btn.setArrowType(Qt.ArrowType.DownArrow)
        self.arrow_btn.setCheckable(True)
        self.arrow_btn.setChecked(True)
        self.header_layout.addWidget(self.arrow_btn)

        self.main_layout.addWidget(self.header)

        # Content area
        self.content = QWidget()
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(12, 0, 12, 12)
        self.main_layout.addWidget(self.content)

        self.arrow_btn.clicked.connect(self._arrow_clicked)
        self.header.mousePressEvent = self._header_clicked

        self.expanded = True

    def _header_clicked(self, event):
        self.toggle()

    def _arrow_clicked(self):
        self.toggle()

    def toggle(self, expand=None):
        if expand is None:
            expand = not self.expanded
        if self.expanded == expand:
            return
        self.expanded = expand
        self.arrow_btn.setArrowType(
            Qt.ArrowType.DownArrow if expand else Qt.ArrowType.RightArrow
        )
        self.content.setVisible(expand)
        self.toggled.emit(expand)

    def sizeHint(self):
        h = self.header.sizeHint().height()
        if self.expanded:
            h += self.content.sizeHint().height()
        w = max(self.header.sizeHint().width(), self.content.sizeHint().width())
        return QSize(w, h)

class LoggerSection(AccordionSection):
    def __init__(self, parent=None):
        super().__init__("mvLogger", icon=None, parent=parent)
        # Top controls
        controls = QHBoxLayout()
        controls.setSpacing(8)
        self.autoscroll = QCheckBox("Auto-scroll")
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setFlat(True)
        self.clear_btn.setStyleSheet("color: #4FC3F7; background: transparent;")
        controls.addWidget(self.autoscroll)
        controls.addWidget(self.clear_btn)
        controls.addStretch()
        controls_widget = QWidget()
        controls_widget.setLayout(controls)
        self.content_layout.addWidget(controls_widget)

        # Log area
        self.log_area = QTextEdit()
        self.log_area.setPlainText("Process Start")
        self.log_area.setStyleSheet("background: #23232b; color: #f7b955; border: 1px solid #4FC3F7;")
        self.content_layout.addWidget(self.log_area)

        # Example badge
        badge_layout = QHBoxLayout()
        badge_layout.addStretch()
        badge = QLabel("34")
        badge.setStyleSheet("""
            background: #4FC3F7; color: white; border-radius: 6px; padding: 2px 6px;
            font-weight: bold;
        """)
        badge2 = QLabel("34")
        badge2.setStyleSheet("""
            background: #4FC3F7; color: white; border-radius: 6px; padding: 2px 6px;
            font-weight: bold;
        """)
        badge_layout.addWidget(badge)
        badge_layout.addWidget(badge2)
        badge_widget = QWidget()
        badge_widget.setLayout(badge_layout)
        self.content_layout.addWidget(badge_widget)

class SettingsSection(AccordionSection):
    def __init__(self, parent=None):
        super().__init__("Setting", icon=None, parent=parent)
        # Example content
        self.content_layout.addWidget(QLabel("Settings go here..."))

class AccordionDockWidget(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("Accordion Dock", parent)
        self.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable | QDockWidget.DockWidgetFeature.DockWidgetFloatable)
        self.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(8)

        self.logger_section = LoggerSection()
        self.settings_section = SettingsSection()
        self.settings_section.toggle(False)  # Start collapsed

        self.main_layout.addWidget(self.logger_section)
        self.main_layout.addWidget(self.settings_section)
        self.main_layout.addStretch()

        self.setWidget(self.main_widget)

        # Accordion behavior: only one open at a time
        self.logger_section.toggled.connect(self._logger_toggled)
        self.settings_section.toggled.connect(self._settings_toggled)

        # Style
        self.setStyleSheet("""
            QDockWidget {
                background: #23232b;
                color: #f7b955;
                border: none;
            }
            #AccordionHeader {
                background: #2d2d37;
                border-radius: 8px;
                font-weight: bold;
            }
            QLabel, QCheckBox {
                color: #f7b955;
            }
            QToolButton {
                background: transparent;
                border: none;
            }
        """)

        # Initial height adjustment
        self._adjust_height()

    def _logger_toggled(self, expanded):
        if expanded:
            self.settings_section.toggle(False)
        self._adjust_height()

    def _settings_toggled(self, expanded):
        if expanded:
            self.logger_section.toggle(False)
        self._adjust_height()

    def _adjust_height(self):
        # Adjust dock height to fit the open section
        total_height = 0
        for section in [self.logger_section, self.settings_section]:
            total_height += section.header.sizeHint().height()
            if section.expanded:
                total_height += section.content.sizeHint().height()
        self.setMinimumHeight(total_height + 24)
        self.setMaximumHeight(total_height + 24)

#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mw = QMainWindow()
#     dock = AccordionDockWidget(mw)
#     mw.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)
#     mw.setStyleSheet("background: #23232b;")
#     mw.resize(320, 480)
#     mw.show()
#     sys.exit(app.exec())