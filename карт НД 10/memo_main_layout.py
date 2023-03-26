from memo_edit_layout import *

wdgt_edit = QWidget()
wdgt_edit.setLayout(layout_from)

list_question = QListView()

btn_add = QPushButton("Нове питання")
btn_delete = QPushButton("Видалити питання")
btn_start = QPushButton("Почати")

main_col1 = QVBoxLayout()
main_col1.addWidget(list_question)
main_col1.addWidget(btn_add)

main_col2 = QVBoxLayout()
main_col2.addWidget(wdgt_edit)
main_col2.addWidget(btn_delete)

main_line1 = QHBoxLayout()
main_line1.addLayout(main_col1)
main_line1.addLayout(main_col2)

main_line2 = QHBoxLayout()
main_line2.addStretch(1)
main_line2.addWidget(btn_start, stretch=2)
main_line2.addStretch(1)

layout_main = QVBoxLayout()
layout_main.addLayout(main_line1)
layout_main.addLayout(main_line2)
