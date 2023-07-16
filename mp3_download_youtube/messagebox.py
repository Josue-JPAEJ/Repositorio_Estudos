from PyQt5.QtWidgets import *


def show_info_messagebox(mensagem: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    # setting message for Message Box
    msg.setText("Information: " + mensagem)

    # setting Message box window title
    msg.setWindowTitle("Information MessageBox")

    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok)

    # start the app
    msg.exec_()


def show_warning_messagebox(mensagem: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)

    # setting message for Message Box
    msg.setText("Warning: " + mensagem)

    # setting Message box window title
    msg.setWindowTitle("Warning MessageBox")

    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok)

    # start the app
    msg.exec_()


def show_question_messagebox(mensagem: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)

    # setting message for Message Box
    msg.setText("Question: " + mensagem)

    # setting Message box window title
    msg.setWindowTitle("Question MessageBox")

    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok)

    # start the app
    msg.exec_()


def show_critical_messagebox(mensagem: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    # setting message for Message Box
    msg.setText("Critical: " + mensagem)

    # setting Message box window title
    msg.setWindowTitle("Critical MessageBox")

    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok)

    # start the app
    msg.exec_()
