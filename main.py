succeful_third_answer = "in"
succeful_second_answer = "am"
succeful_first_answer = "is"
counter = 0
сounter_answer = 0
counter_proc = 0
print("Привет! Предлагаю проверить свои знания английского!Напиши, как тебя зовут?")
name = input()

def guestion(questi:str,succeful_answer:str):
    global counter
    global сounter_answer
    global counter_proc

    print("Привет " + name)
    print("Напишите правильный ответ")
    print(questi)

    answer_1 = input()

    if answer_1 == succeful_answer:
        print("My name is" + name + ", ты + 10 баллов получил!")
        counter = counter + 10
        сounter_answer = сounter_answer + 1
    else:
        print("Ошибочка, ты, не заработал 10 баллов ")
    return



answers = [succeful_first_answer, succeful_second_answer, succeful_third_answer]
questions = ["My name __ ", "I ___ a coder.", "I live __ Moscow"]

for index, velue in enumerate(questions):
    guestion(velue,answers[index])



one_answer_in_proc = 100.0 / float(сounter_answer)
counter_proc = one_answer_in_proc * сounter_answer

print()

if сounter_answer == 1:
    answerov = ' вопрос'
else:
    answerov = ' Vоprosav'

if сounter_answer >= 2:
    answerov = ' Вопроса'

сounter_answer = str(сounter_answer)
procamswer = 30 / 100
answer = procamswer * float(counter)
answer = answer * 10
answer = str(answer)
counter = str(counter)

if counter_proc > 70:
    counter_proc = 100
counter_proc = str(counter_proc)

print("Вот и всё, " + name)
print("Вы ответили на " + сounter_answer + answerov)
print("Вы заработали " + counter + " балов")
print('Это ' + counter_proc + '% успеха')
print("Это круто")
