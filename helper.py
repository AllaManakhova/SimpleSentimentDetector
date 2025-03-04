import os

directory = ""

files = os.listdir(directory)

with open("", mode="w", encoding='utf-8') as f:
    for elem in files:
        f.write("'" + elem + "',\n")
