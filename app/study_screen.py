from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont, QKeySequence, QShortcut
from PyQt6.QtWidgets import(
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
)
from app.screen import Screen
from app.ui_style import *


dummy_cards = [
    {
        "word" : "apple",
        "transcription" : "[æpl]",
        "translation"   : "яблоко",
        "definition"    : "a round, edible fruit.",
        "examples"      : "she ate an <i>apple</i> for breakfast."
    },
    {
        "word" : "car",
        "transcription" : "[kɑː]",
        "translation"   : "автомобиль",
        "definition"    : "a motor vehicle with wheels (usually, 4)",
        "examples"      : "the <i>car</i> is parket outside"
    },
]


class StudyScreen(Screen):
    goto_end_study_screen = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.place_top()
        self.place_card()
        self.place_bottom_buttons()

        self.set_shortcuts()

        self.reset_session()

    def place_top(self) -> None:
        top_layout = QHBoxLayout()
        self.finish_button = QPushButton("закончить обучение")
        self.finish_button.clicked.connect(self.reset_session)
        self.finish_button.clicked.connect(self.goto_end_study_screen.emit)
        
        self.progress_label = QLabel()
        top_layout.addWidget(self.finish_button)
        top_layout.addStretch()
        top_layout.addWidget(self.progress_label)
        self.main_layout.addLayout(top_layout)

    def place_card(self) -> None:
        card_area_layout = QVBoxLayout()
        card_area_layout.setSpacing(SML_SPACING)
        self.main_layout.addLayout(card_area_layout)

        self.card_button = QPushButton()
        self.card_button.setMinimumHeight(CARD_MIN_HEIGHT)
        self.card_button.setCheckable(False)
        self.card_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.card_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.card_button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        self.card_button.clicked.connect(self.flip_card)


        self.card_label = QLabel(self.card_button)
        self.card_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.card_label.setWordWrap(True)
        self.card_label.setTextFormat(Qt.TextFormat.RichText)
        self.card_label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum,
        )

        card_font = QFont()
        card_font.setPointSize(CARD_FONT_SIZE)
        self.card_label.setFont(card_font)

        card_layout = QVBoxLayout(self.card_button)
        card_layout.addWidget(self.card_label)
        self.card_label.setContentsMargins(CARD_MARGINS)

        card_scroll = QScrollArea()
        card_scroll.setWidgetResizable(True)
        card_scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        card_scroll.setFrameShape(QFrame.Shape.NoFrame)
        card_scroll.setWidget(self.card_button)
        card_area_layout.addWidget(card_scroll)

        hint_label = QLabel("нажмите по карточке или пробел, чтобы перевернуть её")
        hint_label.setStyleSheet("color: gray;")
        hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_area_layout.addWidget(hint_label)

    def place_bottom_buttons(self) -> None:
        bottom_layout = QHBoxLayout()
        self.prev_button = QPushButton("назад")
        self.next_button = QPushButton("вперед")
        self.prev_button.setMinimumHeight(BIG_BUTTON_HEIGHT)
        self.next_button.setMinimumHeight(BIG_BUTTON_HEIGHT)
        self.prev_button.clicked.connect(self.next_study)
        self.next_button.clicked.connect(self.next_study)
        
        bottom_layout.addWidget(self.prev_button)
        bottom_layout.addWidget(self.next_button)
        self.main_layout.addLayout(bottom_layout)

    def set_shortcuts(self) -> None:
        shortcuts = [
            ("Space", self.card_button.click),
            ("Left",  self.prev_button.click),
            ("A",     self.prev_button.click),
            ("Right", self.next_button.click),
            ("D",     self.next_button.click),
            ("Esc",   self.finish_button.click),
        ]

        for key, slot in shortcuts:
            sc = QShortcut(QKeySequence(key), self)
            sc.activated.connect(slot)

    def reset_session(self) -> None:
        self.current_card_index = 0
        self.reset_card()

    def reset_card(self) -> None:
        self.is_front_face = True
        self.was_flipped = False

        self.refresh()

    def flip_card(self) -> None:
        self.is_front_face = not self.is_front_face
        self.was_flipped = True

        self.refresh()

    def refresh(self) -> None:
        self.refresh_card()

        self.progress_label.setText(
            f"{self.current_card_index + 1}/{len(dummy_cards)}"
        )

        self.prev_button.setEnabled(self.was_flipped)
        self.next_button.setEnabled(self.was_flipped)

        flip_card_hint = None if self.was_flipped else "переверните карточку"
        self.prev_button.setToolTip(flip_card_hint)
        self.next_button.setToolTip(flip_card_hint)

    def refresh_card(self) -> None:
        current_card = dummy_cards[self.current_card_index]
        
        if self.is_front_face:
            text = (
                "<b>{word}</b><br>"
                "{transcription}" 
            )
        else:
            text = (
                "<b>перевод</b><br>"
                "{translation}<br><br>"
                "<b>определение</b><br>"
                "{definition}<br><br>"
                "<b>примеры использования</b><br>"
                "{examples}"
            )
        self.card_label.setText(text.format_map(current_card))

    def next_study(self) -> None:

        if self.current_card_index < len(dummy_cards) - 1 :
            self.current_card_index += 1
            self.reset_card()
        else:
            self.reset_session()
            self.goto_end_study_screen.emit()

class EndStudyScreen(Screen):
    goto_start_screen = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.place_title(
            "вы закончили обученине",
            "вот ваша статистика по пройденой сессии"
        )
        self.main_layout.addStretch()
        self.place_stats()
        self.place_bottom()

    def place_stats(self) -> None:
        pass

    def place_bottom(self) -> None:
        self.back_button = QPushButton("вернуться на главный экран")
        self.back_button.setMinimumHeight(BIG_BUTTON_HEIGHT)
        self.back_button.clicked.connect(self.goto_start_screen.emit)
        self.main_layout.addWidget(self.back_button)
    