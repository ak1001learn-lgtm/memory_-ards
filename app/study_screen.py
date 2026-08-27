from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import(
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


class StudyScreen(QWidget):
    goto_start_screen = pyqtSignal()

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
        card_area.setCursor(Qt.CursorShape.PointingHandCursor)
        card_area.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )


        card_label = QLabel(card_area)
        card_label.setText("apple")
        card_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card_font = QFont()
        card_font.setPointSize(14)
        card_label.setFont(card_font)

        card_layout = QVBoxLayout(card_area)
        card_layout.addWidget(card_label)

        card_scroll = QScrollArea()
        card_scroll.setWidgetResizable(True)
        card_scroll.setWidget(card_area)
        layout.addWidget(card_scroll)

        hint_label = QLabel("нажмите по карточке или пробел, чтобы перевернуть её")
        hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(hint_label)

        botton_layout = QHBoxLayout()
        prev_button = QPushButton("назад")
        next_button = QPushButton("вперед")
        
        botton_button_hight = 40
        next_button.setMinimumHeight(botton_button_hight)
        botton_layout.addWidget(prev_button)
        prev_button.setMinimumHeight(botton_button_hight)
        botton_layout.addWidget(next_button)
        layout.addLayout(botton_layout)