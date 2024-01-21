
from PyQt5.QtWidgets import (QApplication, QWidget,QLabel,QPushButton,QTabWidget,QSlider,QSpinBox,
                             QVBoxLayout,QHBoxLayout,QLineEdit,QListWidget,QComboBox,QProgressBar, QDial)

from PyQt5.QtCore import Qt 

app = QApplication([])
window = QWidget()
############
tab1 = QWidget()
slider = QSlider()
progress = QProgressBar()
progress.setValue(0)


v1 = QVBoxLayout()
v1.addWidget(slider)
v1.addWidget(progress)
tab1.setLayout(v1)
#################3



################
tab2 = QWidget()
q = QDial()

v2 = QVBoxLayout()
v2.addWidget(q)
tab2.setLayout(v2)
##################

tab3 = QWidget()
s = QSpinBox()
v3 = QVBoxLayout()
v3.addWidget(s)
tab3.setLayout(v3)


tabs = QTabWidget()
tabs.addTab(tab1,'Вкладка №1')
tabs.addTab(tab2,'Вкладка №1')
tabs.addTab(tab3,'Вкладка №1')


v4 = QVBoxLayout()
v4.addWidget(tabs)
window.setLayout(v4)


slider.valueChanged.connect(lambda value:progress.setValue(value) )



window.show()
app.exec()