from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QDockWidget, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton


class AccordionDockWidget(QDockWidget):

    def __init__(self):
        super().__init__()

        self.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea)
        # self.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)

        self.original_height = 0
        self.collapsed = True


        # Main dock widget content
        self.content = QLabel("Dock Content Here")
        content_wrapper = QWidget()
        content_layout = QVBoxLayout(content_wrapper)
        content_layout.setContentsMargins(5, 5, 5, 5)
        content_layout.addWidget(self.content)
        content_layout.addWidget(QLabel("TEST"))
        content_layout.addWidget(QLabel("TEST"))
        content_layout.addWidget(QLabel("TEST"))
        self.setWidget(content_wrapper)

        # Custom title bar
        self.setTitleBarWidget(self.create_title_bar())
        self.setStyleSheet("""
        border: 1px solid #FFFFFF
        """)

    def create_title_bar(self):
        bar = QWidget()
        layout = QHBoxLayout(bar)
        # layout.setContentsMargins(5, 2, 5, 2)

        title = QLabel("mvLogger")
        layout.addWidget(title)

        # layout.addStretch()

        self.arrow_btn = QPushButton()

        qIcon = QIcon()
        img = ":newPrefix/images/" + "fe_arrow-up.png"
        qIcon.addPixmap(QPixmap(img))

        self.arrow_btn.setIcon(qIcon)  # Use your own icons
        self.arrow_btn.setFixedSize(20, 20)
        self.arrow_btn.setFlat(True)
        self.arrow_btn.clicked.connect(self.toggle_vertical_accordion)
        layout.addWidget(self.arrow_btn)

        return bar


    def toggle_vertical_accordion(self):

        print(self.height())
        self.setMaximumHeight(0)

        # if not self.collapsed:
        #     print("up ", self.collapsed)
        #     self.original_height = self.height()
        #     self.setMaximumHeight(30)
        #     qIcon = QIcon()
        #     img = ":newPrefix/images/" + "fe_arrow-up.png"
        #     qIcon.addPixmap(QPixmap(img))
        #     self.arrow_btn.setIcon(qIcon)  # Collapsed icon
        #     self.collapsed = True
        # else:
        #     print("down ", self.collapsed)
        #     self.setMaximumHeight(16777215)
        #     self.resize(self.width(), self.original_height)
        #     qIcon = QIcon()
        #     img = ":newPrefix/images/" + "fe_arrow-up.png"
        #     qIcon.addPixmap(QPixmap(img))
        #     self.arrow_btn.setIcon(qIcon)  # Expanded icon
        #     self.collapsed = False

