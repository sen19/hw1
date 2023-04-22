print("Привет! Предлагаю проверить свои знания английского! Расскажи, как тебя зовут!")

name = input("Введите своё имя\n")
print(f"Привет, {name} , начинаем тренировку!")
correct_answers = 0
score = 0
percent_of_correct = 0
question = ("")

print("")
print("Заполните правильно пробелы")
print("")
print("Первый вопрос:")
print("My name ___ Vova ")
answer_1 = input()

if answer_1 == "is":
    print("Ответ верный! Вы получаете 10 баллов!")
    correct_answers += 1
    score += 10
    percent_of_correct += 33.3
else:
    print("Неправильно. Правильный ответ: is ")

print("")
print("Второй вопрос:")
print("I ___ a coder")
answer_2 = input()

if answer_2 == "am":
    print("Ответ верный! Вы получаете 10 баллов!")
    correct_answers += 1
    score += 10
    percent_of_correct += 33.3
else:
    print("Неправильно. Правильный ответ: am ")

print("")
print("Третий Вопрос:")
print("I live ___ Moscow")
answer_3 = input()

if answer_3 == "in":
    print("Ответ верный! Вы получаете 10 баллов!")
    correct_answers += 1
    score += 10
    percent_of_correct += 33.3
else:
    print("Неправильно. Правильный ответ: in ")

if correct_answers == 3:
    question += ("все вопросы")
elif correct_answers == 2:
    question += ("2 вопроса из 3")
elif correct_answers == 1:
    question += ("1 вопрос из 3")
else:
    question += ("0 вопросов из 3")

print("")
print(f"Вот и все, {name}! ")
print("")
print(f"Вы ответили на {question} верно.")
print("")
print(f"Вы заработали {score} баллов.")
print("")
print(f"Это {round(percent_of_correct)} процентов")
print("")
print(f"Вот и все!\nВы ответили на {question} верно.\nВы заработали {score} баллов.\nЭто {round(percent_of_correct)} процентов")
