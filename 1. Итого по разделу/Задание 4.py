# Напишите программу, которая считывает целое положительное число n, n∈[1;9] и
# выводит значение числа n + nn + nnn

[print(int(i) + int(i * 2) + int(i * 3)) for i in input()]