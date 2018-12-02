import re

def newton1():
  with open('words.txt', encoding='utf-8') as f:
    words = []
    for line in f:
        words.append(line.strip())
 

  print(len([x for x in words if re.search(r"'s$", x)]))

def newton2():
  with open('words.txt', encoding='utf-8') as f:
    words = []
    for line in f:
        words.append(line.strip())
 

  print(len([x for x in words if re.search(r"^Mac[A-Z]", x)] + [x for x in words if re.search(r"^Mc[A-Z]", x)]))

def module3():
  with open('words.txt', encoding='utf-8') as f:
    words = []
    for line in f:
        words.append(line.strip())
 

  print(len([x for x in words if re.search(r"d[^e]{1,}e[^f]{1,}f[^g]{1,}g", x)]))

def newton4():
  with open('words.txt', encoding='utf-8') as f:
    words = []
    for line in f:
        words.append(line.strip())


  print(len([x for x in words if re.search(r"q[^u]", x)]))

def newton5():
  with open('words.txt', encoding='utf-8') as f:
    words = []
    for line in f:
        words.append(line.strip())
 

  print(len([x for x in words if re.search(r"d.{0,}e.{0,}f.{0,}g", x)]))

if __name__ == "__main__":
  newton5()