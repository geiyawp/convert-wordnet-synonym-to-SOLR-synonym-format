from collections import defaultdict
import codecs

dd = defaultdict(list)
a = "[]''&.%#@!$^*)(-=+?:;/"
content = []
new_line = {}


with open("syn.txt", "r", encoding="utf-8") as f:   # open synonym file
    for line in f:
        z = line.rstrip("\n").split("\t", 3)
        key = z[0]
        value = z[3]
        new_line = {key: value}
        content.append(new_line)


for d in content:
    for key, value in d.items():
        dd[key].append(value)

#removing any special character
def cleaning(raw_string):
    for char in a:
        raw_string = raw_string.replace(char, "")
    return raw_string

#writing the results to a new file
with open("syn_final2.txt", "w", encoding="utf-8") as text_file:
    for items in dd:
        x = dd[items]
        yolo = str(x)
        b = cleaning(yolo)
        print(b, file=text_file)
