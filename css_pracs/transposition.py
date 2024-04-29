from math import ceil
import pprint

ip = input("Enter an input string : ")
print(len(ip))
cols = 4
rows = ceil(len(ip) / cols)

matrix = [['x'] * cols for _ in range(rows)]

pointer = 0
for i in range(rows):
    for j in range(cols):
        if pointer < len(ip):
            matrix[i][j] = ip[pointer]
            pointer += 1

pprint.pp(matrix)

e = ""

for i in range(cols):
    for j in range(rows):
        e += matrix[j][i]

print(e)
