from PyQt6 import QtWidgets
from Controller.UnderviserGUI import UnderviserGUI
from Controller.SekretarGUI import SekretarGUI
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    Underviser_window = UnderviserGUI()
    Sekretar_window = SekretarGUI()
    app.exec()

if __name__ == '__main__':
    main()