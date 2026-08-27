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


class StartScreen(QWidget):
    goto_study_screen = pyqtSignal()
    quit_app          = pyqtSignal()


    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            layout_margin := 40,
            layout_margin,
            layout_margin,
            layout_margin,
        )
        layout.setSpacing(16)

        title = QLabel("memory cards")
        title_font = QFont()
        title_font.setPointSize(22)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)

        subtitle = QLabel("изучаем английский с помощью карточек")
        layout.addWidget(subtitle)

        study_button = QPushButton("начать обучение")
        study_button.setMinimumHeight(40)
        study_button.clicked.connect(self.goto_study_screen.emit)
        layout.addWidget(study_button)

        modes_label = QLabel("режим обучения")
        layout.addWidget(modes_label)

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
        moeds_layout = QHBoxLayout()

        for radio in mode_radios:
            mode_group.addButton(radio)
            moeds_layout.addWidget(radio)

        layout.addLayout(moeds_layout)

        tags_label = QLabel("категории:")
        layout.addWidget(tags_label)

        tags_container = QWidget()
        self.tags_layout = QVBoxLayout(tags_container)
        self.tags_layout.setContentsMargins(
            tags_layout_mardin := 10,
            tags_layout_mardin,
            tags_layout_mardin,
            tags_layout_mardin
        )

        tags_scroll = QScrollArea()
        tags_scroll.setWidgetResizable(True)
        tags_scroll.setWidget(tags_container)
        layout.addWidget(tags_scroll)

        settings_button = QPushButton("настойки")
        quit_button    = QPushButton("выйти")
        quit_button.clicked.connect(self.quit_app.emit)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(settings_button)
        bottom_layout.addWidget(quit_button)
        layout.addLayout(bottom_layout)

        self.refresh_tags()

    def refresh_tags(self):
        dummy_tags = [
            "транспорт",
            "природа",
            "школа",
            "спорт",
        ]

        dummy_tags.sort()
        for tag_name in dummy_tags:
            check = QCheckBox(tag_name.lower())
            self.tags_layout.addWidget(check)
