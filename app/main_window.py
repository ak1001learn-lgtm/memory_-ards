from PyQt6.QtWidgets import QMainWindow, QStackedWidget 

from app.settings_screen import SettingsScreen
from app.start_screen import StartScreen
from app.study_screen import EndStudyScreen, StudyScreen

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("mamory cards")   


        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack) 

        self.start_screen     = StartScreen()
        self.study_screen     = StudyScreen()
        self.end_study_screen = EndStudyScreen()
        self.settings_screen   = SettingsScreen()

        self.stack.addWidget(self.start_screen)
        self.stack.addWidget(self.study_screen)
        self.stack.addWidget(self.end_study_screen)
        self.stack.addWidget(self.settings_screen)

        self.open_start()

        self.start_screen.goto_study_screen.connect(self.open_study)
        self.start_screen.quit_app.connect(self.close)
        self.start_screen.goto_settings_screen.connect(self.open_settings)

        self.study_screen.goto_end_study_screen.connect(self.open_end_study)

        self.end_study_screen.goto_start_screen.connect(self.open_start)

        self.settings_screen.goto_start_screen.connect(self.open_start)

    def open_start(self) -> None:
        self.stack.setCurrentWidget(self.start_screen)
    
    def open_study(self) -> None:
        #self.study_screen.reset_session()
        self.stack.setCurrentWidget(self.study_screen)

    def open_end_study(self) -> None:
        self.stack.setCurrentWidget(self.end_study_screen)

    def open_settings(self) -> None:
        self.stack.setCurrentWidget(self.settings_screen)
