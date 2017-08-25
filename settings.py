from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Settings(QWidget):
    def __init__(self, R, r, d, type):
        super().__init__()
        self.initUi(R, r, d, type)

    def initUi(self, R, r, d, type):
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.setMinimumSize(QSize(250, 180))
        self.setMaximumSize(QSize(250, 180))
        self.setWindowTitle("Settings")

        self.button = QPushButton("Redraw")

        vbox = QVBoxLayout()
        
        label1 = QLabel("Set big radius R: ")
        label2 = QLabel("Set small radius r: ")
        label3 = QLabel("Set distance d: ")

        hbox1 = QHBoxLayout()
        self.slider1 = QSlider(0x1)
        spin1 = QSpinBox()
        self.slider1.setMaximum(200)
        spin1.setMaximum(200)
        self.slider1.valueChanged.connect(spin1.setValue)
        spin1.valueChanged.connect(self.slider1.setValue)
        hbox1.addWidget(self.slider1)
        hbox1.addWidget(spin1)
        self.slider1.setValue(R)

        hbox2 = QHBoxLayout()
        self.slider2 = QSlider(0x1)
        spin2 = QSpinBox()
        self.slider2.setMaximum(200)
        spin2.setMaximum(200)
        self.slider2.valueChanged.connect(spin2.setValue)
        spin2.valueChanged.connect(self.slider2.setValue)
        hbox2.addWidget(self.slider2)
        hbox2.addWidget(spin2)
        self.slider2.setValue(r)

        hbox3 = QHBoxLayout()
        self.slider3 = QSlider(0x1)
        spin3 = QSpinBox()
        self.slider3.setMaximum(200)
        spin3.setMaximum(200)
        self.slider3.valueChanged.connect(spin3.setValue)
        spin3.valueChanged.connect(self.slider3.setValue)
        hbox3.addWidget(self.slider3)
        hbox3.addWidget(spin3)
        self.slider3.setValue(d)

        hbox4 = QHBoxLayout()
        self.button = QPushButton("Redraw")
        self.type = QComboBox()
        self.type.addItem("Hypotrochoid")
        self.type.addItem("Epitrochoid")
        self.type.addItem("Hypocycloid")
        self.type.setCurrentIndex(type - 1)
        
        hbox4.addWidget(self.type)
        hbox4.addStretch(1)
        hbox4.addWidget(self.button)

        vbox.addWidget(label1)
        vbox.addLayout(hbox1)

        vbox.addWidget(label2)
        vbox.addLayout(hbox2)

        vbox.addWidget(label3)
        vbox.addLayout(hbox3)

        vbox.addLayout(hbox4)

        self.setLayout(vbox)
        self.show()
        
        x, y = self.geometry().x(), self.geometry().y()
        self.move(x - 400, y)
