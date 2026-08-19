from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import  (
    QButtonGroup,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QVBoxLayout, 
    QWidget
)


class StartScreen(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout(self)


        title = QLabel("memory cards")
        title_font = QFont()
        title_font.setPointSize(22)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)

        subtitle = QLabel("изучаем английский с помощью карточек")
        layout.addWidget(subtitle)

        layout.addSpacing(12)

        study_button = QPushButton("начать обучение")
        study_button.setMinimumHeight(40)
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

        # moeds_layout.addStretch()
        layout.addLayout(moeds_layout)

        # QCheckBox для тегов
        #QScrollArea 

        settings_button = QPushButton("настойки")
        quit_button    = QPushButton("выйти")

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(settings_button)
        bottom_layout.addWidget(quit_button)
        layout.addLayout(bottom_layout)
