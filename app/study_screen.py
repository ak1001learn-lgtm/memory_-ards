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


CARD_MIN_HEIGHT = 280
CARD_PADDING    = 16

dummy_cards = [
    {
        "world" : "apple",
        "transcription" : "[æpl]",
        "translation"   : "яблоко",
        "definition"    : "a round, edible fruit.",
        "examples"      : "she ate an <i>apple</i> for breakfast."
    },
    {
        "world" : "car",
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

        self.is_front_face = True
        self.was_flipped = False 

        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            layout_margin := 40,
            layout_margin,
            layout_margin,
            layout_margin,
        )
        layout.setSpacing(16)

        top_layout = QHBoxLayout()
        back_button = QPushButton("на главный экран")
        back_button.clicked.connect(self.goto_start_screen.emit)
        progress_label = QLabel("40/120")
        top_layout.addWidget(back_button)
        top_layout.addStretch()
        top_layout.addWidget(progress_label)
        layout.addLayout(top_layout)

        card_area = QPushButton()
        card_area.setMinimumHeight(CARD_MIN_HEIGHT)
        card_area.setCheckable(False)
        #card_area.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        card_area.setCursor(Qt.CursorShape.PointingHandCursor)
        card_area.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        card_area.clicked.connect(self.flip_card)


        self.card_label = QLabel(card_area)
        self.card_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.card_label.setWordWrap(True)
        self.card_label.setTextFormat(Qt.TextFormat.RichText)
        self.card_label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum,
        )

        card_font = QFont()
        card_font.setPointSize(14)
        self.card_label.setFont(card_font)

        card_layout = QVBoxLayout(card_area)
        card_layout.addWidget(self.card_label)
        self.card_label.setContentsMargins(
            CARD_PADDING, 
            CARD_PADDING, 
            CARD_PADDING, 
            CARD_PADDING,
        )

        card_scroll = QScrollArea()
        card_scroll.setWidgetResizable(True)
        card_scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        card_scroll.setFrameShape(QFrame.Shape.NoFrame)
        card_scroll.setWidget(card_area)
        layout.addWidget(card_scroll)

        hint_label = QLabel("нажмите по карточке или пробел, чтобы перевернуть её")
        hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(hint_label)

        botton_layout = QHBoxLayout()
        self.prev_button = QPushButton("назад")
        self.next_button = QPushButton("вперед")
        
        self.next_button.setMinimumHeight(botton_button_hight :=40)
        botton_layout.addWidget(self.prev_button)
        self.prev_button.setMinimumHeight(botton_button_hight)
        botton_layout.addWidget(self.next_button)
        layout.addLayout(botton_layout)

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
        
        if self.is_front_face:
            text = (
                "<b>Apple</b><br>"
                "[æpl]" 
            )
        else:
            text = (
                "<b>перевод</b><br>"
                "яблоко<br><br>"
                "<b>определение</b><br>"
                "a round, edible fruit.<br><br>"
                "<b>примеры использования</b><br>"
                "she ate an <i>apple</i> for breakfast."
            )
        self.card_label.setText(text)