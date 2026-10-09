
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import  (
    QLabel,
    QVBoxLayout, 
    QWidget
)

from app.ui_style import *


class Screen(QWidget):
    def __init__ (self) -> None:
        super().__init__()

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(BIG_MARGINS)
        self.main_layout.setSpacing(BIG_SPACING)

    def place_title(self, title: str, subtitle: str) -> None:
        title_layout = QVBoxLayout()
        title_layout.setSpacing(SML_SPACING)
        self.main_layout.addLayout(title_layout)

        title_label = QLabel("memory cards")
        title_font = QFont()
        title_font.setPointSize(TITLE_FONT_SIZE)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_layout.addWidget(title_label)

        subtitle_label = QLabel("изучаем английский с помощью карточек")
        title_layout.addWidget(subtitle_label)