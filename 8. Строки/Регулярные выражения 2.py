'''
Извлечь из текста все числа.
Числа могут быть отрицательные, вещественные, целые.
'''
from re import *

text = open('input.txt').read()

nums = findall(r'\-?\d+\.?\d*', text)
print(*nums)