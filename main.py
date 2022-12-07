from collections import OrderedDict

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys

import module_Popup as new
import branch as brn


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.w = None
        self.uso = None
        self.previous_name = None
        self.item = None
        self.root = None
        self.branch = 0
        self.name = ''
        self.num = 1
        self.rack = 1
        self.module = 1
        self.elements = []

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
        self.tree.setStyleSheet(brn.STYLESHEET)
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(['USO'])
        self.tree.clicked.connect(self.onClicked)
        self.tree.doubleClicked.connect(self.save_previous_name)
        self.tree.itemChanged.connect(self.current_item_changed)
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
        self.file_Menu.addAction(self.add_rack)
        self.file_Menu.addAction(self.add_module)

    def _createActions(self):
        self.newAction = QAction("Добавить шкаф", self)
        self.newAction.triggered.connect(self.add_uso)
        self.delete_one = QAction("Удалить", self)
        self.delete_one.triggered.connect(lambda: self.del_element(parent=self.tree.currentItem()))
        self.add_rack = QAction("Добавить корзину", self)
        self.add_rack.triggered.connect(self.add_new_rack)
        self.add_module = QAction("Добавить модуль", self)
        self.add_module.triggered.connect(self.add_new_module)

        self.add_rack.setVisible(False)
        self.add_module.setVisible(False)

    def add_uso(self):
        if self.branch == 0:
            self.add_rack.setVisible(True)
            name = 'New_USO-' + str(self.num)
            self.root = QTreeWidgetItem()
            self.root.setText(0, name)
            self.root.setFlags(self.root.flags() | QtCore.Qt.ItemIsEditable)
            self.elements.append(self.root)
            self.num += 1
            # # Загрузить все свойства и элементы управления корневого узла
            self.tree.addTopLevelItem(self.root)

    def onClicked(self):
        self.item = self.tree.currentItem()
        self.branch = 0
        try:
            if self.item.parent():
                self.branch = 1
                try:
                    if self.item.parent().parent():
                        self.branch = 2
                except:
                    pass
        except:
            pass

    def add_new_rack(self):
        self.add_module.setVisible(True)
        if self.branch == 0:
            text = self.item.text(0)
            ra = 'rack' + str(self.rack)
            try:
                child1 = QTreeWidgetItem()
                child1.setText(0, ra)
                child1.setFlags(child1.flags() | QtCore.Qt.ItemIsEditable)
                rt = self.item
                rt.addChild(child1)
                self.rack += 1
            except [AttributeError, KeyError]:
                pass

    def get_module(self):
        text = self.item.parent().text(0)
        mod = 'module' + str(self.module)
        child1 = QTreeWidgetItem()
        child1.setText(0, mod)
        child1.setFlags(child1.flags() | QtCore.Qt.ItemIsEditable)
        rt = self.item
        rt.addChild(child1)
        self.module += 1

    def add_new_module(self):
        if self.branch == 1:
            self.w = new.ModulesWindow(self)
            self.w.show()
            self.get_module()

    def current_item_changed(self):
        if self.item is not None:
            print(self.previous_name, self.item.text(0), sep=' ---> ')

    def save_previous_name(self):
        self.previous_name = self.item.text(0)

    def del_element(self, parent=None):
        rt = self.tree.invisibleRootItem()
        for it in self.tree.selectedItems():
            (it.parent() or rt).removeChild(it)

        if len(self.elements) == 0:
            self.add_rack.setVisible(False)
        print(self.elements)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    sys.exit(app.exec_())
