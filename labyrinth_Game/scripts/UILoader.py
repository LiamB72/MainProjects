from scripts.variables import *


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi("scripts\lab.ui", self)
        self.setFixedSize(self.size())
        self.startButton.clicked.connect(self.buttonStart)

        self.show()

    def buttonStart(self):
        global difficulty

        if self.diffNormal.isChecked():
            print("Difficulty selected : Normal")
            difficulty = 1

        if self.diffHard.isChecked():
            print("Difficulty selected : Hard")
            difficulty = 2

        self.close()


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()
