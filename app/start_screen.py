from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import  (
    QButtonGroup,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QVBoxLayout, 
    QWidget
)

from app.screen import*
from app.ui_style import *


dummy_tags = [
    "транспорт",
    "природа",
    "школа",
    "спорт",
]

class StartScreen(Screen):
    goto_study_screen = pyqtSignal()
    quit_app          = pyqtSignal()


    def __init__(self) -> None:
        super().__init__()

        self.place_title(
            "memory cards",
            "изучаем английский с помощью карточек"
        )
        self.place_study_button()
        self.place_modes()
        self.place_tags()
        self.place_bottom_buttons()

        self.refresh_tags()

    def place_study_button(self) -> None:
        self.study_button = QPushButton("Начать обучение")
        self.study_button.setMinimumHeight(BIG_BUTTON_HEIGHT)
        self.study_button.clicked.connect(self.goto_study_screen.emit)
        self.main_layout.addWidget(self.study_button)

    def place_modes(self) -> None:
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
    
    def place_tags(self) -> None:
        tags_layout = QVBoxLayout()
        tags_layout.setSpacing(SML_SPACING)
        self.main_layout.addLayout(tags_layout)

        tags_label = QLabel("категории:")
        tags_layout.addWidget(tags_label)

        tags_select_layout = QHBoxLayout()
        tags_layout.addLayout(tags_select_layout)

        self.tags_search = QLineEdit()
        self.tags_search.setPlaceholderText("поиск по категориям...")
        self.tags_search.setClearButtonEnabled(True)
        self.tags_search.textChanged.connect(self.filter_tags)
        tags_select_layout.addWidget(self.tags_search)

        self.select_all_button   = QPushButton("выбрать все")
        self.deselect_all_button = QPushButton("снять все")
        self.select_all_button.clicked.connect(lambda: self.set_visible_tags_checked(True))
        self.deselect_all_button.clicked.connect(lambda: self.set_visible_tags_checked(False))
        tags_select_layout.addWidget(self.select_all_button)
        tags_select_layout.addWidget(self.deselect_all_button) 

        tags_container = QWidget()
        self.tags_scroll_layout = QVBoxLayout(tags_container)
        self.tags_scroll_layout.setContentsMargins(SML_MARGINS)
        self.tags_scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.no_tags_label = QLabel("ничего не найдено")
        self.no_tags_label.setStyleSheet("color: gray; font-style: italic;")
        self.no_tags_label.setVisible(False)
        self.tags_scroll_layout.addWidget(self.no_tags_label)

        tags_scroll = QScrollArea()
        tags_scroll.setWidgetResizable(True)
        tags_scroll.setWidget(tags_container)
        tags_layout.addWidget(tags_scroll)

    def place_bottom_buttons(self) -> None:
        settings_button = QPushButton("настойки")
        quit_button    = QPushButton("выйти")
        quit_button.clicked.connect(self.quit_app.emit)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(settings_button)
        bottom_layout.addWidget(quit_button)
        self.main_layout.addLayout(bottom_layout) 

    def refresh_tags(self) -> None:
        dummy_tags.sort()
        self.tags_checkboxes: list[QCheckBox] = []

        for tag_name in dummy_tags:
            check = QCheckBox(tag_name.lower())
            check.toggled.connect(self.refresh_study_button)
            
            self.tags_checkboxes.append(check)
            self.tags_scroll_layout.addWidget(check)

        self.refresh_study_button()

    def refresh_study_button(self) -> None:
        any_checkt = any(check.isChecked()for check in self.tags_checkboxes)
        
        self.study_button.setEnabled(any_checkt)
        self.study_button.setToolTip(None if any_checkt else "выберите хотя бы одну категорию")

    def filter_tags(self, search_text: str) -> None:
        search_text = search_text.lower()
        any_visible = False

        for check in self.tags_checkboxes:
            is_match = search_text in check.text()
            check.setVisible(is_match)
            any_visible = any_visible or is_match

        self.select_all_button.setEnabled(any_visible)
        self.deselect_all_button.setEnabled(any_visible)

        no_tags_hint = None if any_visible else "нет видимых категорий"
        self.select_all_button.setToolTip(no_tags_hint)
        self.deselect_all_button.setToolTip(no_tags_hint)

        self.no_tags_label.setVisible(not any_visible)

    def set_visible_tags_checked(self, cheched: bool) -> None:
        for check in self.tags_checkboxes:
            if check.isVisible():
                check.setChecked(cheched)
