import os
import re

# Prompt user to enter file's location and name
Loc = input("Enter the file's location(Path):".strip())
os.chdir(Loc)
file = input("Enter the file's name:".strip())

# Open files
sysFile = open(file, "r")
output = open("find.txt", "w")

# Prompt user what to search
search = input("Enter what to search:".strip())

# Read the file
count = 0
for line in sysFile:
    line = line.rstrip()
    if re.search(search, line, re.IGNORECASE):
        output.write(line)
        output.write("\n")
        count = count + 1

print("Lines found: ", count)
