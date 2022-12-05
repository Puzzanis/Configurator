from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('Config')
        self.setGeometry(250, 200, 1300, 700)
        self.setMinimumSize(1300, 700)
        # Add Menu
        self._createActions()
        self._createMenuBar()

        layout_left = QVBoxLayout()
        layout_right = QHBoxLayout()
        layout_central = QHBoxLayout()

        self.tree = QTreeWidget()
        self.tree.setMinimumWidth(200)
        layout_left.addWidget(self.tree)

        tab1 = QTableWidget()
        layout_right.addWidget(tab1)

        layout_central.addLayout(layout_left)
        layout_central.addLayout(layout_right)

        main_widget = QSplitter(QtCore.Qt.Horizontal)
        main_widget.setLayout(layout_central)
        self.setCentralWidget(main_widget)

    def _createMenuBar(self):
        self.menu_Bar = self.menuBar()
        self.file_Menu = QMenu("Управление", self)
        self.menu_Bar.addMenu(self.file_Menu)
        # self.newAction = QAction("Добавить", self)
        self.file_Menu.addAction(self.newAction)
        self.file_Menu.addAction(self.delete_one)
        # self.file_Menu.addAction(self.delete_all)

    def _createActions(self):
        self.newAction = QAction("Добавить шкаф", self)
        # self.newAction.triggered.connect(self.add_element)
        self.delete_one = QAction("Удалить шкаф", self)
        # self.delete_one.triggered.connect(self.del_element)
        # self.delete_all = QAction("Удалить все элементы", self)
        # self.delete_all.triggered.connect(self.del_all_elements)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    sys.exit(app.exec_())

