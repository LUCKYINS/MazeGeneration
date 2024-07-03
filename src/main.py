"""
    Coder: Luckyyyin
"""
from PySide6.QtWidgets import QApplication
from src.maze import MazeGeneration

if __name__ == "__main__":
    app = QApplication()
    app.setStyleSheet("""
                       QWidget{
                           background-color:white;
                       }
                       """)
    window = MazeGeneration()
    window.show()
    app.exec()