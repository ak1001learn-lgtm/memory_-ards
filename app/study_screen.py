from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import(
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget
)

class StudyScreen(QWidget):
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
        progress_label = QLabel("40/120")
        top_layout.addWidget(back_button)
        top_layout.addStretch()
        top_layout.addWidget(progress_label)
        layout.addLayout(top_layout)

        card_area = QPushButton()

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