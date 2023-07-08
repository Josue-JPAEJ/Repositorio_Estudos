import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from ui_login import Ui_Form


class GuiContinuacaoLogin (QMainWindow, Ui_Form):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    view = GuiContinuacaoLogin()
    view.show()
    qt.exec()

