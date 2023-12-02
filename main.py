import io
import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>400</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>300</y>
      <width>174</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>Сделать окружность</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>400</width>
     <height>36</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Repo(QMainWindow):
    def __init__(self):
        super().__init__()

        f = io.StringIO(template)
        uic.loadUi(f, self)  # загружаем дизайн
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        x, y = 100, 100
        w = randint(10, 200)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, w, w)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Repo()
    ex.show()
    sys.exit(app.exec())

