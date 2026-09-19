from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import(
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget
)

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


class StudyScreen(QWidget):
    goto_start_screen = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(BIG_MARGINS)
        self.main_layout.setSpacing(BIG_SPACING)

        self.place_top()
        self.place_card()
        self.place_bottom_buttons()

        self.reset_session()

    def place_top(self) -> None:
        top_layout = QHBoxLayout()
        back_button = QPushButton("на главный экран")
        back_button.clicked.connect(self.reset_session)
        back_button.clicked.connect(self.goto_start_screen.emit)
        progress_label = QLabel("40/120")
        top_layout.addWidget(back_button)
        top_layout.addStretch()
        top_layout.addWidget(progress_label)
        self.main_layout.addLayout(top_layout)

    def place_card(self) -> None:
        card_area_layout = QVBoxLayout()
        card_area_layout.setSpacing(SML_SPACING)
        self.main_layout.addLayout(card_area_layout)

        card_button = QPushButton()
        card_button.setMinimumHeight(CARD_MIN_HEIGHT)
        card_button.setCheckable(False)
        #card_area.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        card_button.setCursor(Qt.CursorShape.PointingHandCursor)
        card_button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        card_button.clicked.connect(self.flip_card)


        self.card_label = QLabel(card_button)
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

        card_layout = QVBoxLayout(card_button)
        card_layout.addWidget(self.card_label)
        self.card_label.setContentsMargins(CARD_MARGINS)

        card_scroll = QScrollArea()
        card_scroll.setWidgetResizable(True)
        card_scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        card_scroll.setFrameShape(QFrame.Shape.NoFrame)
        card_scroll.setWidget(card_button)
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

    def reset_session(self) -> None:
        self.current_card_index = 0
        self.reset_card()

    def reset_card(self) -> None:
        self.is_front_face = True
        self.was_flipped = False

        self.update()

    def flip_card(self) -> None:
        self.is_front_face = not self.is_front_face
        self.was_flipped = True

        self.update()

    def update(self) -> None:
        self.update_card()
        self.prev_button.setEnabled(self.was_flipped)
        self.next_button.setEnabled(self.was_flipped)

    def update_card(self) -> None:
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
            self.goto_start_screen.emit()