
succeful_third_answer = "in"
succeful_second_answer = "am"
succeful_first_answer = "is"
counter = 0
сounter_answer = 0
counter_proc = 0
print ("Привет! Предлагаю проверить свои знания английского!Напиши, как тебя зовут?")

name = input()

print("Привет " + name)
print("Напишите правильный ответ")
print("My name __ " + name)

answer_1 = input()

if answer_1 == succeful_first_answer:
  print ("My name is" + name +", ты + 10 баллов получил!")
  counter = counter+10
  сounter_answer = сounter_answer + 1
  counter_proc = counter_proc + 33
else:
   print("Ошибочка, ты, не заработал 10 баллов ")

print("I ___ a coder.")

answer_2 = input()

if answer_2 == succeful_second_answer:
  print ("I am a coder." + name +", ты + 10 баллов получил!")
  counter = counter+10
  сounter_answer = сounter_answer + 1
  counter_proc = counter_proc + 33

else:
   print("Ошибочка, ты, не заработал 10 баллов ")

print("I live __ Moscow")

answer_3 = input()

if answer_3 == succeful_third_answer:
  print ("I live ___ Moscow" + name +", ты + 10 баллов получил!")
  counter = counter+10
  сounter_answer = сounter_answer + 1
  counter_proc = counter_proc + 33

else:
   print("Ошибочка, ты, не заработал 10 баллов ")

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



go




print("Вот и всё, " + name )
print("Вы ответили на " + сounter_answer + answerov)
print("Вы заработали " + counter + " балов")
print('Это ' + counter_proc + '% успеха')
print("Это круто")