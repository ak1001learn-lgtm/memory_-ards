from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import(
    QPushButton,
)

from app.screen import Screen
from app.ui_style import *


class SettingsScreen(Screen):
    goto_start_screen = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.main_layout.addStretch()
        self.place_bottom()

    def place_bottom(self) -> None:
        self.save_button = QPushButton("сохранить и вернуться")
        self.save_button.setMinimumHeight(BIG_BUTTON_HEIGHT)
        self.save_button.clicked.connect(self.goto_start_screen.emit)
        self.main_layout.addWidget(self.save_button)
    