from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from random import randint, shuffle

text_wrong = 'Неверно'
text_correct = 'Верно'
new_quest_templ = 'Новый вопрос' # такая строка будет устанавливаться по умолчанию для новых вопросов
new_answer_templ = 'Новый ответ' # то же для ответов

class Question():
    ''' хранит информацию про одну анкетку'''
    def __init__(self, question=new_quest_templ, answer=new_answer_templ, 
                       wrong_answer1='', wrong_answer2='', wrong_answer3=''):
        self.question = question # вопрос
        self.answer = answer # правильный ответ
        self.wrong_answer1 = wrong_answer1 # считаем, что всегда пишется три неверных варианта
        self.wrong_answer2 = wrong_answer2 # 
        self.wrong_answer3 = wrong_answer3 #
        self.is_active = True # продолжать ли задавать этот вопрос?
        self.attempts = 0 # сколько раз этот вопрос задавался
        self.correct = 0 # количество верных ответов
    def got_right(self):
        ''' меняет статистику, получив правильный ответ'''
        self.attempts += 1
        self.correct += 1
    def got_wrong(self):
        ''' меняет статистику, получив неверный ответ'''
        self.attempts += 1

class QuestionView():
    ''' сопоставляет данные и виджеты для визуализации анкеты
    этот класс и его наследники похожи на то, что делает QDataWidgetMapper 
    детям лучше обойтись без дополнительного абстрактного класса, 
    а прописывать конкретно связь с элементами нашей формы'''
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        # конструктор получает и запоминает объект с данными и виджеты, соответствующие полям анкеты
        self.frm_model = frm_model  # может получить и None - ничего страшного не случится, 
                                    # но для метода show нужно будет предварительно обновить данные методом change
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3  
    def change(self, frm_model):
        ''' обновление данных, уже связанных с интерфейсом '''
        self.frm_model = frm_model
    def show(self):
        ''' выводит на экран все данные из объекта '''
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)


class AnswerCheck(QuestionView):

    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3,showed_answer,result):
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.showed_answer = showed_answer
        self.result = result

    def check(self):  
        if self.answer.isChecked():
            self.result.setText(text_correct) # надпись "верно" или "неверно"
            self.showed_answer.setText(self.frm_model.answer) # пишем сам текст ответа в соотв. виджете 
            self.frm_model.got_right() # обновить статистику, добавив один верный ответ
        else:
            self.result.setText(text_wrong) # надпись "верно" или "неверно"
            self.showed_answer.setText(self.frm_model.answer) # пишем сам текст ответа в соотв. виджете 
            self.frm_model.got_wrong() # обновить статистику, добавив неверный ответ
            

class QuestionListModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_list = list()
    def rowCount(self):
        return len(self.form_list)

    def data(self, index, role):
        
        if role == Qt.DisplayRole:
            form = self.form_list[index.row()]
            return form.question
    
    def insertRows(self,parent = QModelIndex):

        position = self.rowCount() 
        self.beginInsertRows(parent, position, position)
        self.form_list.append(Question()) 
        self.endInsertRows() 
        QModelIndex()
        return True

    def removeRows(self, position, parent=QModelIndex()):
        self.beginRemoveRows(parent, position, position)
        self.form_list.pop(position)
        self.endRemoveRows() 
        return True

    def random_question(self):

        return self.form_list[randint(0,self.rowCount() - 1)]

    
def random_AnswerCheck(list_model, w_question, widgets_list, w_showed_answer, w_result):
    '''возвращает новый экземпляр класса AnswerCheck, 
    со случайным вопросом и случайным разбросом ответов по виджетам'''
    frm = list_model.random_question()
    shuffle(widgets_list)
    frm_card = AnswerCheck(frm, w_question, widgets_list[0], widgets_list[1], widgets_list[2], widgets_list[3], w_showed_answer, w_result)
    return frm_card