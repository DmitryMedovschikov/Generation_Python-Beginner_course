# Напишите программу, которая выводит на экран текст «Здравствуй, мир!»
# (без кавычек).

print('Здравствуй, мир!')

# Напишите программу, которая выводит последовательность чисел: 4 8 15 16 23
# 42 с одним пробелом между ними.

print('4', '8', '15', '16', '23', '42')

# Напишите программу, которая выводит последовательность чисел: 4 8 15 16 23
# 42 каждое на отдельной строке.

lst = [4, 8, 15, 16, 23, 42]
[print(i) for i in lst]

# Напишите программу, которая выводит указанный треугольник, состоящий из
# звездочек (*).

[print('*' * i) for i in range(1, 8)]

#  Напишите программу, которая выводит на экран приветствие в виде слова
#  «Привет» (без кавычек), после которого должна стоять запятая и пробел, а
#  затем введенное имя.

print('Привет', input())

# На вход программе подается строка текста – название футбольной команды.
# Напишите программу, которая повторяет ее на экране со словами « - чемпион!»
# (без кавычек).

print(input(), '- чемпион!')

# Напишите программу, которая считывает три строки по очереди, а затем выводит
# их в той же последовательности, каждую на отдельной строчке.

[print(input()) for n in range(3)]

# Напишите программу, которая считывает три строки по очереди, а затем выводит
# их в обратной последовательности, каждую на отдельной строчке.

print(*reversed([input() for i in range(3)]), sep='\n')
