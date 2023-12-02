import io
import sys
from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt

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
        self.setGeometry(300, 300, 400, 400)  # задаём расположение и размеры окна
        self.label = QLabel()  
        canvas = QPixmap(200, 200)
        self.label.setPixmap(canvas)
        self.pushButton.clicked.connect(self.click)
    
    def click(self):
        x, y = 200, 200
        w, h = [randint(10, 100) for i in range(2)]        
        # создаем экземпляр QPainter, передавая холст (self.label.pixmap())
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('YELLOW'))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Repo()
    ex.show()
    sys.exit(app.exec())

