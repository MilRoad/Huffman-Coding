from huffman import HuffmanCoding
import sys
import random
import string
import time


# генерация входных данных в виде строки
def randomString(stringLength=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(stringLength))


# ввод размера строки
n = int(input('Введите размер строки:     '))

with open("sample.txt", "w") as file:
    print(randomString(n), file=file)

path = "sample.txt"

h = HuffmanCoding(path)
start = time.time()
output_path = h.compress()
print("время затраченное на работу (в секундах): ", time.time()-start)