# Напишите программу, которая выводит на экран текст «I***like***Python» (без
# кавычек).

print('I', 'like', 'Python', sep='***')

# Напишите программу, которая считывает строку-разделитель и три строки,
# а затем выводит указанные строки через разделитель.

lst = [input() for i in range(4)]
print(*lst[1:], sep=lst[0])

# Напишите программу, которая приветствует пользователя, выводя слово
# «Привет» (без кавычек), после которого должна стоять запятая и пробел,
# а затем введенное имя и восклицательный знак.

print('Привет,', input(), end='!')
