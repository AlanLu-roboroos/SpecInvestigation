from sys import argv
from math import floor, ceil
import pyperclip

with open(argv[1], "r") as f:
    data = f.readlines()


out = []
num = int(argv[2])
for i in range(0, num):
    out.append([])

if len(argv) <= 3:
    for idx in range(0, len(data)):
        temp = data[idx].split()
        for i in range(0, num):
            out[i].append(float(temp[i]))
else:
    for idx in range(0, len(data), floor(len(data)/int(argv[3]))):
        temp = data[idx].split()
        for i in range(0, num):
            out[i].append(float(temp[i]))

def pl(idx):
    text = ""
    for i in out[idx]:
        text += f"{i}\n"
    pyperclip.copy(text)
