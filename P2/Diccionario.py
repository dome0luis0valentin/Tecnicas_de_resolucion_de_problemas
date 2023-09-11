import sys

dict_words = {}

line = sys.stdin.readline()

while (line != "\n"):
    
    word = line.split()[0]
    trad = line.split()[1]
    dict_words.append(word: trad)
    line = sys.stdin.readline()

line = sys.stdin.readline()
while line:
    msg = line
    try:
        sys.stdout.write(dict_words[msg])
    except (KeyError):
        sys.stdout.write("eh")
    
