# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, \
    QPushButton, QMessageBox, QDesktopWidget, QLabel, QHBoxLayout, \
    QVBoxLayout, QGridLayout, QLineEdit, QTextEdit, QMainWindow, \
    QAction, qApp
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class CodyIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

class Cody_Tips(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        button = QPushButton('Button', self)
        button.setToolTip('This is a <b>QPushButton</b> widget')
        button.resize(button.sizeHint())
        button.move(50, 50)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

class Cody_Widget_Close(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        bttn = QPushButton('Quit', self)
        bttn.clicked.connect(QCoreApplication.instance().quit)
        bttn.resize(bttn.sizeHint())

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit Button')
        self.show()

class Cody_Messeges(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message Box')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class Cody_Center_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 250)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Cody_Absolute_Layout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lb1 = QLabel('Zetcode', self)
        lb1.move(15, 10)

        lb2 = QLabel('tutorials', self)
        lb2.move(35, 40)

        lb3 = QLabel('for programers', self)
        lb3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()

class Cody_Boxlayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

class Cody_Gridlayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9',
                 '/', '4', '5', '6', '*', '1', '2', '3',
                 '-', '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

class Cody_Gridlayout1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Auther')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

class Cody_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('StatusBar')
        self.show()

class Cody_MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('MenuBar')
        self.show()

class Cody_Toolbar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()

class Cody_ManuToolBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main Window')
        self.show()

def Cody():
    print('In cody function......')
    #app = QApplication(sys.argv)
    #w = QWidget()
    #w.resize(250, 150)
    #w.move(300, 300)
    #w.setWindowTitle('Test')
    #w.show()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = CodyIcon()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_Tips()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_Widget_Close()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_Messeges()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_Center_Window()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_Absolute_Layout()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_Boxlayout()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_Gridlayout()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_Gridlayout1()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_MainWindow()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_MainWindow1()
    #sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #ex = Cody_Toolbar()
    #sys.exit(app.exec_())

    app = QApplication(sys.argv)
    ex = Cody_ManuToolBar()
    sys.exit(app.exec_())


if __name__ == '__main__':
    Cody()
