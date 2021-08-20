# Ползователь вводите числа и операторы.
# The user's inputs for the numbers and the operators
num_1 = float(input('Введите первое число: '))
operator = input('Введите оператор: ')
num_2 = float(input('Введите второе число: '))

# Операторы (+ | - | * | /)
# if Operators is (+ | - | * | /) then print out numbers
if operator == '+':
    print(num_1 + num_2)
if operator == '-':
    print(num_1 - num_2)
if operator == '*':
    print(num_1 * num_2)
if operator == '/':
    print(num_1 / num_2)

# Ползователь не ввел оператор
# if the user didn't put an operator
else:
    print('Оператор не найден')