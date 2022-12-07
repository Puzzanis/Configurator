from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import branch as brn


class ModulesWindow(QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.main = root

        self.setFixedHeight(817)
        self.setFixedWidth(975)

        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()

        layout_central = QHBoxLayout()

        self.tree = QTreeWidget()
        self.tree.invisibleRootItem()
        self.tree.setRootIsDecorated(False)
        self.tree.setStyleSheet(brn.STYLESHEET)
        self.tree.setMinimumWidth(200)
        self.tree.setColumnCount(1)

        self.root = QTreeWidgetItem()
        self.root.setText(0, 'Modicon M580')
        self.tree.addTopLevelItem(self.root)

        layout_left.addWidget(self.tree)

        bt_ok = QPushButton('OK')
        bt_cancel = QPushButton('Cancel')

        layout_right.addWidget(bt_ok)
        layout_right.addWidget(bt_cancel)
        layout_right.addStretch(1)

        layout_central.addLayout(layout_left)
        layout_central.addLayout(layout_right)

        main_widget = QSplitter(QtCore.Qt.Horizontal)
        main_widget.setLayout(layout_central)
        layout_central.addWidget(main_widget)

        main_widget.setLayout(layout_central)
        self.setLayout(layout_central)

