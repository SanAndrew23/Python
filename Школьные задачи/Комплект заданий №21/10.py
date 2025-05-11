def first_last(line):
    words = line.split()
    print(f'{words[0]} {words[-1]}')


line = input()
first_last(line)