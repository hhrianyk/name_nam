from PyQt5.QtWidgets import QWidget
from random import shuffle # будем перемешивать ответы в карточке вопроса

from memo_app import app
from memo_data import Form, FormView

from memo_card_layout import *
 
main_width, main_height = 800, 450 # начальные размеры главного окна

text_wrong = 'Неверно'
text_correct = "Верно"

# пока еще работаем с одним вопросом, а не списком вопросов. Создаем:
frm = Question('Питання1', 'Правильна відповідь', 'НЕ Правильна відповідь1', 'НЕ Правильна відповідь2', 'НЕ Правильна відповідь3')

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)  # перемешиваем варианты ответа
# связываем эту информацию с формой ответа на вопрос:
frm_card = QuestionView(frm, lb_Question, radio_list[0], radio_list[1], radio_list[2], radio_list[3])
 
def check_result():
    ''' проверка, правильный ли ответ выбран
    если ответ был выбран, то надпись "верно/неверно" приобретает нужное значение
    и показывается панель ответов '''
    # по-хорошему имеет смысл сделать наследника FormModel c этой функцией, потому что тут есть завязки и на интерфейс, и на данные...
    correct = frm_card.answer.isChecked() # в этом радиобаттоне лежит наш ответик!
    if correct:
        # ответ верный, запишем 
        lb_Result.setText(text_correct) # надпись "верно" или "неверно"
        lb_Correct.setText(frm_card.answer.text()) # это приходится делать вручную
        show_result()
    else:
        incorrect = frm_card.wrong_answer1.isChecked() or frm_card.wrong_answer2.isChecked() or frm_card.wrong_answer3.isChecked()
        if incorrect:
            # ответ неверный, запишем и отразим в статистике
            lb_Result.setText(text_wrong) # надпись "верно" или "неверно"
            lb_Correct.setText(frm_card.answer.text()) # это приходится делать вручную
            show_result()

def click_OK(self):
    # пока что проверяем вопрос, если мы в режиме вопроса, иначе ничего
    if btn_OK.text() != 'Следующий':
        check_result()

btn_OK.clicked.connect(click_OK)

win_card = QWidget()
win_card.resize(main_width, main_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')
win_card.setLayout(layout_card)
frm_card.show()
# show_data() вместо этого используем методы объектов, связывающих формы с данными:
show_question()

win_card.show()
app.exec_()