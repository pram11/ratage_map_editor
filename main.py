import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map Editor Prototype")
        self.resize(800, 600)
        
        label = QLabel("PySide6 맵 에디터가 정상적으로 설정되었습니다.", self)
        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
