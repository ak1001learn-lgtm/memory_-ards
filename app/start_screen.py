from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import  (
    QLabel,
    QPushButton,
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
        study_button.setMinimumHeight(48)
        layout.addWidget(study_button)