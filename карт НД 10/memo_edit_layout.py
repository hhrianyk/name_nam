from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from memo_app import *

txt_Question = QLineEdit("")
txt_Answer = QLineEdit("")
txt_Wrong = QLineEdit("")
txt_Wrong2 = QLineEdit("")
txt_Wrong3 = QLineEdit("")

layout_from = QFormLayout()

layout_from.addRow("Питання: ", txt_Question)
layout_from.addRow("Dslgjdslm: ", txt_Answer)
layout_from.addRow("Неправильна відповідь: ", txt_Wrong)
layout_from.addRow("Неправильна відповідь2: ", txt_Wrong2)
layout_from.addRow("Неправильна відповідь3: ", txt_Wrong3)