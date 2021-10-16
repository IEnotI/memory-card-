#отображение окна приложения 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QRadioButton,QMessageBox,QGroupBox,QButtonGroup
from random import *
#обработк
class Question():#cоздание класса
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3
def show_answer():
    RadioGroup.hide()
    RadioGroup2.show()
    button.setText('Cледущий вопрос')
def show_question():
    RadioGroup.show()
    RadioGroup2.hide()
    button.setText('Ответить')
    button_group.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    button_group.setExclusive(True)
def start():
    if button.text()=='Ответить':
        show_answer()
        check_answer()
    else:
        next_question()
#создание элементов интерфейса
app=QApplication([])
main_win=QWidget()
main_win.resize(1250,720)
main_win.setWindowTitle('Определите победителя')
#button=QPushButton('Сгенерировать')
text=QLabel('Какой год ближе к 2000')
right_answerlabel=QLabel("Тут будет правильный ответ")
result=QLabel('Правильно/Неправильно')
RadioGroup=QGroupBox("Выбери ответ")
RadioGroup2=QGroupBox("Результат теста")
answer1=QRadioButton('2005')
answer2=QRadioButton('2010')
answer3=QRadioButton('2015')
answer4=QRadioButton('2020')
button_group=QButtonGroup()
button_group.addButton(answer1)
button_group.addButton(answer2)
button_group.addButton(answer3)
button_group.addButton(answer4)
button=QPushButton('Ответить')
answers=[answer1,answer2,answer3,answer4]
def ask(q:Question):# задаём вопрос правильный ответ и 3 неправильных ответа
    text.setText(q.question)
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    right_answerlabel.setText(q.right_answer)
    show_question()
def check_answer():#проверка ответа
    if answers[0].isChecked():
        result.setText('Правильно')
    else:
        result.setText("Неверно")
    right_answerlabel.setText(answers[0].text())
'''def show_correct():
    right_answer.setText('Правильно')
    right_answer.show'''
#пивяза элементов к вертикальной линии
grouplayout2=QVBoxLayout()
grouplayout=QVBoxLayout()
mainlayout=QVBoxLayout()
mainlayout.addWidget(text)
mainlayout.addWidget(RadioGroup)
mainlayout.addWidget(RadioGroup2)
mainlayout.addWidget(button)
grouplayout.addWidget(answer1)
grouplayout.addWidget(answer2)
grouplayout.addWidget(answer3)
grouplayout.addWidget(answer4)
grouplayout2.addWidget(result)
grouplayout2.addWidget(right_answerlabel)
RadioGroup.setLayout(grouplayout)
RadioGroup2.setLayout(grouplayout2)

 
main_win.setLayout(mainlayout)
RadioGroup2.hide()
#обработка событий
button.clicked.connect(start)


#запуск приложения'''
q=Question("Какого цвета нет",'1','2','3','4')  
question_list=[]
question_list.append(q)
question_list.append(Question('2+3','5','3','6','4'))
question_list.append(Question('2+3','5','4','6','2'))
main_win.cur_question=-1
ask(q)
def next_question():#следущтй вопрос
    main_win.cur_question=randint(0,len(question_list)-1)
    
    q = question_list[main_win.cur_question]
    ask(q)
main_win.show()
app.exec_()