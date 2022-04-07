from PyQt6 import QtWidgets
from Underviser import Underviser
from UnderviserGUI import UnderviserGUI
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    new_employee_window = UnderviserGUI()
    app.exec()

if __name__ == '__main__':
    main()