from PyQt5 import QtCore, QtWidgets
import sys

from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 196)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 581, 51))
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(150, 90, 291, 24))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setMinimumSize(QtCore.QSize(91, 0))
        self.label_2.setObjectName("label_2")
        self.txtEntradaTemperatura = QtWidgets.QLineEdit(self.splitter)
        self.txtEntradaTemperatura.setMinimumSize(QtCore.QSize(191, 0))
        self.txtEntradaTemperatura.setStyleSheet("border-radius: 5px;")
        self.txtEntradaTemperatura.setAlignment(QtCore.Qt.AlignCenter)
        self.txtEntradaTemperatura.setObjectName("txtEntradaTemperatura")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(200, 150, 201, 28))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.btnConverter = QtWidgets.QPushButton(self.splitter_2)
        self.btnConverter.setObjectName("btnConverter")
        self.btnSair = QtWidgets.QPushButton(self.splitter_2)
        self.btnSair.setObjectName("btnSair")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnSair.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnConverter.clicked.connect(self.converte)

    def converte(self):
        try:
            temp = int(self.txtEntradaTemperatura.text())
            temp = (temp - 32) * 5 / 9
            msg = QMessageBox()
            msg.setIcon(msg.Information)
            msg.setWindowTitle("Sucesso")
            msg.setText(f"Resultado: {str(temp)} ºC")
            msg.exec()

        except Exception as erro:
            msg = QMessageBox()
            msg.setIcon(msg.Warning)
            msg.setWindowTitle("Erro")
            msg.setText(f"Insira dados válidos. Erro  {erro}")
            msg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conversor F/C - versão 1.0"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\">Conversor de Temperatura Fahrenheit (ºF) para Celcius (ºC)</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Temperatura:"))
        self.btnConverter.setText(_translate("MainWindow", "Converter"))
        self.btnSair.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
