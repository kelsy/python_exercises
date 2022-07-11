import re

name = input("Enter a file:")
if len(name) < 1:
    name = "regex_sum_42.txt"

try:
    handle = open(name)
except:
    print("File could not be opened:", name)
    quit()

total = 0
for line in handle:
    matches = re.findall('[0-9]+', line)
    total += sum([int(num) for num in matches])

print(total)