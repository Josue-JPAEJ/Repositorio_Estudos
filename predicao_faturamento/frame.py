import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from os.path import dirname, relpath, join
import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AutoReg
from tkinter import Tk
from tkinter.filedialog import askopenfilename


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lb_totalFaturado = QtWidgets.QLabel(self.centralwidget)
        self.lb_totalFaturado.setMinimumSize(QtCore.QSize(137, 16))
        self.lb_totalFaturado.setMaximumSize(QtCore.QSize(137, 16))
        self.lb_totalFaturado.setObjectName("lb_totalFaturado")
        self.verticalLayout_2.addWidget(self.lb_totalFaturado)
        self.txt_totalFaturado = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_totalFaturado.setMinimumSize(QtCore.QSize(137, 22))
        self.txt_totalFaturado.setMaximumSize(QtCore.QSize(137, 22))
        self.txt_totalFaturado.setObjectName("txt_totalFaturado")
        self.verticalLayout_2.addWidget(self.txt_totalFaturado)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_media = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_media.setChecked(True)
        self.rb_media.setObjectName("rb_media")
        self.verticalLayout.addWidget(self.rb_media)
        self.rb_desvioPadrao = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_desvioPadrao.setObjectName("rb_desvioPadrao")
        self.verticalLayout.addWidget(self.rb_desvioPadrao)
        self.rb_mediaPonderada = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_mediaPonderada.setObjectName("rb_mediaPonderada")
        self.verticalLayout.addWidget(self.rb_mediaPonderada)
        self.rb_segregacaoDados = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_segregacaoDados.setObjectName("rb_segregacaoDados")
        self.verticalLayout.addWidget(self.rb_segregacaoDados)
        self.rb_regressaoLinear = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_regressaoLinear.setObjectName("rb_regressaoLinear")
        self.verticalLayout.addWidget(self.rb_regressaoLinear)
        self.rb_seriesTemporais = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_seriesTemporais.setObjectName("rb_seriesTemporais")
        self.verticalLayout.addWidget(self.rb_seriesTemporais)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_predicao = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_predicao.setMinimumSize(QtCore.QSize(640, 0))
        self.txt_predicao.setObjectName("txt_predicao")
        self.horizontalLayout.addWidget(self.txt_predicao)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_predizer = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_predizer.setFont(font)
        self.btn_predizer.setObjectName("btn_predizer")
        self.horizontalLayout.addWidget(self.btn_predizer)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 4)
        self.spb_colunas = QtWidgets.QSpinBox(self.centralwidget)
        self.spb_colunas.setMinimumSize(QtCore.QSize(51, 31))
        self.spb_colunas.setMaximumSize(QtCore.QSize(51, 31))
        self.spb_colunas.setObjectName("spb_colunas")
        self.gridLayout.addWidget(self.spb_colunas, 0, 2, 1, 1)
        self.lb_predicaoFaturamento = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.lb_predicaoFaturamento.setFont(font)
        self.lb_predicaoFaturamento.setObjectName("lb_predicaoFaturamento")
        self.gridLayout.addWidget(self.lb_predicaoFaturamento, 0, 0, 1, 1)
        self.btn_arquivo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_arquivo.setMinimumSize(QtCore.QSize(111, 41))
        self.btn_arquivo.setMaximumSize(QtCore.QSize(111, 41))
        self.btn_arquivo.setObjectName("btn_arquivo")
        self.gridLayout.addWidget(self.btn_arquivo, 0, 3, 1, 1)
        self.tbw_faturamento = QtWidgets.QTableWidget(self.centralwidget)
        self.tbw_faturamento.setMinimumSize(QtCore.QSize(300, 0))
        self.tbw_faturamento.setObjectName("tbw_faturamento")
        self.tbw_faturamento.setColumnCount(3)
        self.tbw_faturamento.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbw_faturamento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbw_faturamento.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbw_faturamento.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tbw_faturamento, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.spb_colunas, self.btn_arquivo)
        MainWindow.setTabOrder(self.btn_arquivo, self.rb_media)
        MainWindow.setTabOrder(self.rb_media, self.rb_desvioPadrao)
        MainWindow.setTabOrder(self.rb_desvioPadrao, self.rb_mediaPonderada)
        MainWindow.setTabOrder(self.rb_mediaPonderada, self.rb_segregacaoDados)
        MainWindow.setTabOrder(self.rb_segregacaoDados, self.rb_regressaoLinear)
        MainWindow.setTabOrder(self.rb_regressaoLinear, self.rb_seriesTemporais)
        MainWindow.setTabOrder(self.rb_seriesTemporais, self.btn_predizer)
        MainWindow.setTabOrder(self.btn_predizer, self.tbw_faturamento)
        MainWindow.setTabOrder(self.tbw_faturamento, self.txt_totalFaturado)
        MainWindow.setTabOrder(self.txt_totalFaturado, self.txt_predicao)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Predição de Faturamento"))
        self.lb_totalFaturado.setText(_translate("MainWindow", "Total faturado"))
        self.label_3.setText(_translate("MainWindow", "Tipo de predição"))
        self.rb_media.setText(_translate("MainWindow", "Média"))
        self.rb_desvioPadrao.setText(_translate("MainWindow", "Desvio padrão"))
        self.rb_mediaPonderada.setText(_translate("MainWindow", "Média ponderada"))
        self.rb_segregacaoDados.setText(_translate("MainWindow", "Segregação de dados"))
        self.rb_regressaoLinear.setText(_translate("MainWindow", "Regressão linear"))
        self.rb_seriesTemporais.setText(_translate("MainWindow", "Séries temporais"))
        self.btn_predizer.setText(_translate("MainWindow", "Predizer"))
        self.lb_predicaoFaturamento.setText(_translate("MainWindow", "Predição de faturamento"))
        self.btn_arquivo.setText(_translate("MainWindow", "Arquivo"))
        item = self.tbw_faturamento.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tbw_faturamento.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ano"))
        item = self.tbw_faturamento.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Faturamento"))
        self.btn_arquivo.clicked.connect(self.openFile)
        self.btn_predizer.clicked.connect(self.predicao)

    def openFile(self):
        # localiza o caminho do arquivo
        Tk().withdraw()
        path = askopenfilename()
        self.all_data = pd.read_csv(path)

        # Carrega o arquivo na tabela tbw_faturamento
        numColumn = self.spb_colunas.value()
        if numColumn == 0:
            numRows = len(self.all_data.index)
        else:
            numRows = numColumn

        self.tbw_faturamento.setColumnCount(len(self.all_data.columns))
        self.tbw_faturamento.setRowCount(numRows)
        self.tbw_faturamento.setHorizontalHeaderLabels(self.all_data)

        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tbw_faturamento.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tbw_faturamento.resizeColumnsToContents()
        self.tbw_faturamento.resizeRowsToContents()

        # soma do faturamento
        soma_faturamento = str(f"R$ {round(sum(self.all_data['Faturamento']), 2)}")
        self.txt_totalFaturado.setText(soma_faturamento)

    def predicao(self):
        df = self.all_data

        # media
        media = df['Faturamento'].mean()
        if self.rb_media.isChecked():
            predicao = 'Nos próximos meses será faturado R$ ' + str('%0.02f' % media) + '/mês em media.'
        elif self.rb_desvioPadrao.isChecked():
            desvio_padrao = df['Faturamento'].std()
            coe_var = (desvio_padrao / media) * 100
            predicao = 'Predição de R$ ' + str('%0.02f' % media) + '/mês podendo variar em torno de ' + str('%0.02f' % coe_var) + '%.'
        elif self.rb_mediaPonderada.isChecked():
            lista = np.transpose((np.array([df['Faturamento'].tail(), np.arange(1, 6)])))
            df_ult = pd.DataFrame(lista, columns=['Ultimos', 'Pesos'])
            df_ult['Ponderado'] = df_ult['Ultimos'] * df_ult['Pesos']
            media_ponderada = df_ult['Ponderado'].sum() / df_ult['Pesos'].sum()
            predicao = 'Predição ponderada de R$ ' + str('%0.02f' % media_ponderada) + ' para os próximos meses.'
        elif self.rb_segregacaoDados.isChecked():
            df_janeiro = df.loc[df['Mes'] == 1]
            media_segregacao = df_janeiro['Faturamento'].mean()
            predicao = 'Predição segregada de R$ ' + str('%0.02f' % media_segregacao) + ' para janeiro.'
        elif self.rb_regressaoLinear.isChecked():
            coefficients = np.polyfit(df.index, df['Faturamento'], 1)
            a = coefficients[0]
            b = coefficients[1]
            jan_reta = a * 36 + b
            predicao = 'Predição por regressão de R$ ' + str('%0.02f' % jan_reta) + ' para janeiro.'
        elif self.rb_seriesTemporais.isChecked():
            model = AutoReg(df['Faturamento'], lags=1)
            model_fit = model.fit()
            yhat = model_fit.predict(len(df['Faturamento']), len(df['Faturamento']) + 2)
            pred = np.array(yhat)
            predicao = 'Predição por série temporal de ' \
                       'R$ ' + str('%0.02f' % pred[0]) + ' para janeiro e ' \
                                                         'R$ ' + str('%0.02f' % pred[1]) + ' para fevereiro. '
        self.txt_predicao.setText(predicao)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
