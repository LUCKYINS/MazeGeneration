"""
    Coder: Luckyyyin
"""
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtGui import QPainter, QColor, QPixmap
from backend import Grid, Maze


class MazeGeneration(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.grid = Grid(24, 24, 1)
        self.canvas = QLabel()
        self.dim = self.grid.dimension
        self.canvas.setStyleSheet("""
                                  QLabel{background-color: black;}
                                  """)
        self.start = QPushButton("start")
        self.start.clicked.connect(self.drawGrid)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.start)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        
    def drawGrid(self):
        self.canvas.resize(self.dim+50, self.dim+50)
        self.map = QPixmap(self.canvas.width(), self.canvas.height())
        self.pen = QPainter(self.map)
        self.pen.setPen(QColor(255,255,255))
        div = self.grid.division
        maze = Maze(self.grid)
        w = self.grid.width
        for node in maze.nodes:
            x,y = node.position
            x *= w
            y *= w
            pos1 = QPoint(x, y)
            if node.up:
                self.pen.drawLine(pos1, QPoint(x,y-w*div))
            elif node.down:
                self.pen.drawLine(pos1,QPoint(x,y+w*div))
            elif node.left:
                self.pen.drawLine(pos1,QPoint(x-w*div,y))
            elif node.right:
                self.pen.drawLine(pos1,QPoint(x+w*div,y))
        self.pen.end()
        self.canvas.setPixmap(self.map)