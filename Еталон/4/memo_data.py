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
