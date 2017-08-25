from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from math import sin, cos

from settings import *

SIZE = 500

class View(QWidget):
	def __init__(self, R, r, d, type):
		super().__init__()
		self.initUi(R, r, d, type)

	def initUi(self, R, r, d, type):
		self.setMinimumSize(QSize(SIZE, SIZE))
		self.setMaximumSize(QSize(SIZE, SIZE))
		self.setWindowTitle("Spirals " + str((R, r, d, type)))

		self.settings = Settings(R, r, d, type)
		self.settings.button.clicked.connect(self.redrawSlot)

		self.alpha = 0 

		self.type = type

		self.R = R
		self.r = r
		self.d = d

		self.points = []

		self.img = QPixmap(500, 500)
		self.img.fill(QColor(255, 255, 255))

		updater = QTimer(self)
		updater.start(1)
		updater.timeout.connect(self.update)

		self.show()


	def degToRad(self, alpha):
		PI = 3.14159265
		return alpha/180.0 * PI

	def getCoords1(self):
		#Гипотрохоида
		R, r, d = self.R, self.r, self.d

		alpha = self.degToRad(self.alpha)
		expr = (R - r) / r * alpha 
		x = (R - r) * cos(alpha) + d * cos(expr)
		y = (R - r) * sin(alpha) - d * sin(expr)

		return (x, y)

	def getCoords2(self):
		#Эпитрохоида
		#d - Отдаление от центра малого круга
		
		R, r, d = self.R, self.r, self.d
		m = r/R

		alpha = self.degToRad(self.alpha)
		x = R * (m + 1) * cos(m*alpha) - d * (cos((m+1)*alpha))
		y = R * (m + 1) * sin(m*alpha) - d * (sin((m+1)*alpha))

		return (x, y)

	def getCoords3(self):
		#Гипоциклоида

		R, r, d = self.R, self.r, self.d
		k = R/r

		alpha = self.degToRad(self.alpha)
		x = r * (k - 1) * (cos(alpha) + (cos((k-1)*alpha))/(k-1))
		y = r * (k - 1) * (sin(alpha) - (sin((k-1)*alpha))/(k-1))

		return (x, y)

	def paintEvent(self, e):
		if self.type == 1:
			x, y = self.getCoords1()
		elif self.type == 2:
			x, y = self.getCoords2()
		elif self.type == 3:
			x, y = self.getCoords3()

		qp = QPainter()

		#draw on image
		qp.begin(self.img)
		qp.drawPoint(250 + x, 250 + y)
		qp.end()

		#draw on screen
		qp.begin(self)
		qp.drawPixmap(QPoint(0,0), self.img)
		qp.end()

		del qp

		self.alpha += 0.75

	def redrawSlot(self):
		self.img.fill(QColor(255, 255, 255))

		self.alpha = 0

		self.R = self.settings.slider1.value()
		self.r = self.settings.slider2.value()
		self.d = self.settings.slider3.value()
		self.type = self.settings.type.currentIndex() + 1

		self.setWindowTitle("Spirals " + str((self.R, self.r, self.d, self.type)))
	
	def closeEvent(self, e):
		del self.settings

app = QApplication([])
view1 = View(100, 40, 80, type=2)
app.exec()
	