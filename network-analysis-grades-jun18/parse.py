import re

# collecting is used as a flag to signify whether the parser should
# read a number from the current line
with open("grades.txt", encoding="utf8") as fp:
    grades = []
    collecting = False
    for line in fp:
        if re.match("- \d -", line): # Grades appear after page number
            collecting = True
        if line[0] == chr(12): # 0x0C = chr(12) = FF = New page character
            collecting = False
        if collecting and re.match("\d{1,2}", line):
            grades.append(int(line))

import collections
counter = collections.Counter(grades) # Calculate frequency table

n = len(grades)

for grade, freq in sorted(counter.items()): # Sort frequency table so that 0..10 grades are shown sequentially
    print("{:2d}: {:3d}  {:6.2f}%".format(grade, freq, (freq * 100 / n)))