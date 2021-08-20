#Импортируем библиотеку рандом
import random
#Даем начальное значение для attempts
attempts = 0
#Ставим границы рандома
numbers = random.randint(1, 20)
print("I am thinking of a number between 1 and 20. ")
#Цикл для ограничения попыток
while attempts < 6:
    guess = int(input("Take a guess: "))
#После каждой попытки attempts увеличивается на 1 до 6 попытки
    attempts += 1
#Если загаданое число меньше введеного то пишем Higher если меньше то lower а если числа равны то мы завершаем цикл
    if guess < numbers:
        print("Higher")
    elif guess > numbers:
        print("Lower")
    elif guess == numbers:
        break
# При введении правильного ответа мы выводим первый отвте, если не правильный то второй варивнт
if guess == numbers:
    attempts = str(attempts)
    print(f"Good Job! You gussed my number in {attempts} guesses!")

if guess != numbers:
    numbers  = str(numbers)
    print(f"Nope. The numbers I was thinking of was {numbers}")