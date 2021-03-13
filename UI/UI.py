import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QTime, QTimerEvent, QDate, QCoreApplication
import time
import csv

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
    
    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()
        self.setCentralWidget(self.table)

        self.timebar = self.statusBar()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updat)
        self.timer.start(1000)
        self.show()


    def updat(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + '/orders.csv', 'r', encoding='utf-8', newline='') as csv_file:
            data = list(csv.reader(csv_file))
            self.table.setFont(QtGui.QFont('SansSerif', 15))

            self.table.setModel(TableModel(data))
            
        self.show_timebar()
        

    def show_timebar(self):
        date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
        time = QTime.currentTime().toString(Qt.DefaultLocaleLongDate)
        self.timebar.showMessage(date + time)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
