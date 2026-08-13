from PyQt6.QtWidgets import QMainWindow, QStackedWidget 

from app.start_screen import StartScreen

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("mamory cards")   


        stack = QStackedWidget()
        self.setCentralWidget(stack) 

        start_screen = StartScreen()

        stack.addWidget(start_screen)