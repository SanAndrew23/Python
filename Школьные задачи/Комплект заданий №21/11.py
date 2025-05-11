line = input()

open_bracket = line.find('(')
closed_bracket = line.find(')')
while open_bracket != -1 and closed_bracket != -1:
    print(line[open_bracket + 1: closed_bracket])
    open_bracket = line.find('(', open_bracket + 1)
    closed_bracket = line.find(')', closed_bracket + 1)

