from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import  (
    QButtonGroup,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QVBoxLayout, 
    QWidget
)

from app.ui_style import *


dummy_tags = [
    "транспорт",
    "природа",
    "школа",
    "спорт",
]

class StartScreen(QWidget):
    goto_study_screen = pyqtSignal()
    quit_app          = pyqtSignal()


    def __init__(self) -> None:
        super().__init__()

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(BIG_MARGINS)
        self.main_layout.setSpacing(BIG_SPACING)

        self.create_title()
        self.create_study_button()
        self.create_modes()
        self.create_tags()
        self.creade_bottom_buttons()

        self.refresh_tags()

    def create_title(self) -> None:
        title_layout = QVBoxLayout()
        title_layout.setSpacing(SML_SPACING)
        self.main_layout.addLayout(title_layout)

        title = QLabel("memory cards")
        title_font = QFont()
        title_font.setPointSize(TITLE_FONT_SIZE)
        title_font.setBold(True)
        title.setFont(title_font)
        title_layout.addWidget(title)

        subtitle = QLabel("изучаем английский с помощью карточек")
        title_layout.addWidget(subtitle)

    def create_study_button(self) -> None:
        study_button = QPushButton("начать обучение")
        study_button.setMinimumHeight(BIG_BUTTON_HEIGHT)
        study_button.clicked.connect(self.goto_study_screen.emit)
        self.main_layout.addWidget(study_button)
    
    def create_modes(self) -> None:
        modes_layout = QVBoxLayout()
        modes_layout.setSpacing(SML_SPACING)
        self.main_layout.addLayout(modes_layout)

        modes_label = QLabel("режим обучения")
        modes_layout.addWidget(modes_label)

        radio_new_only = QRadioButton("только новые")
        radio_all      = QRadioButton("все карточки")
        radio_practice = QRadioButton("новые с повторами")
        radio_new_only.setChecked(True)

        mode_radios = [
            radio_new_only, 
            radio_all,
            radio_practice,
        ]

        mode_group = QButtonGroup(self)
        moeds_group_layout = QHBoxLayout()
        modes_layout.addLayout(moeds_group_layout)

        for radio in mode_radios:
            mode_group.addButton(radio)
            moeds_group_layout.addWidget(radio)
    
    def create_tags(self) -> None:
        tags_layout = QVBoxLayout()
        tags_layout.setSpacing(SML_SPACING)
        self.main_layout.addLayout(tags_layout)

        tags_label = QLabel("категории:")
        tags_layout.addWidget(tags_label)

        tags_container = QWidget()
        self.tags_scroll_layout = QVBoxLayout(tags_container)
        self.tags_scroll_layout.setContentsMargins(SML_MARGINS)

        tags_scroll = QScrollArea()
        tags_scroll.setWidgetResizable(True)
        tags_scroll.setWidget(tags_container)
        tags_layout.addWidget(tags_scroll)

    def creade_bottom_buttons(self) -> None:
        settings_button = QPushButton("настойки")
        quit_button    = QPushButton("выйти")
        quit_button.clicked.connect(self.quit_app.emit)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(settings_button)
        bottom_layout.addWidget(quit_button)
        self.main_layout.addLayout(bottom_layout) 

    def refresh_tags(self) -> None:
        dummy_tags.sort()
        for tag_name in dummy_tags:
            check = QCheckBox(tag_name.lower())
            self.tags_scroll_layout.addWidget(check)
