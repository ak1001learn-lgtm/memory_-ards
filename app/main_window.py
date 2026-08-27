from PyQt6.QtWidgets import QMainWindow, QStackedWidget 

from app.start_screen import StartScreen
from app.study_screen import StudyScreen

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("mamory cards")   


        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack) 

        self.start_screen = StartScreen()
        self.study_screen = StudyScreen()

        self.stack.addWidget(self.start_screen)
        self.stack.addWidget(self.study_screen)

        self.start_screen.goto_study_screen.connect(self._open_study)
        self.start_screen.quit_app.connect(self.close)

        self.study_screen.goto_start_screen.connect(self._open_start)

    def _open_study(self) -> None:
        self.stack.setCurrentWidget(self.study_screen)

    def _open_start(self) -> None:
        self.stack.setCurrentWidget(self.start_screen)
