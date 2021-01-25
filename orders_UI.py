import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QTime, QTimerEvent
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
    def __init__(self, renew = 1):
        super().__init__()
        self.cnt = 0
        self.data = []

        self.table = QtWidgets.QTableView()
        self.setCentralWidget(self.table)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.order_update)
        self.timer.start(renew * 1000)
        self.show()

    def order_update(self):
        with open('orders.csv', 'r', encoding='utf-8', newline='') as csv_file:
            d = list(csv.reader(csv_file))
        self.data = d
        self.model = TableModel(self.data)
        self.table.setModel(self.model)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
