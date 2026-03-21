f_in = open('input.txt', encoding='utf-8')
f_out = open('output.txt', 'w', encoding='utf-8')
w1 = f_in.readline()
w2 = f_in.readline()
words = []
result = []
for line in f_in:
    st = line.split()
    words.append(st)
for word in words:
    if w1 == word:
        result.append(w2)
    else:
        result.append(word)
for i in result:
    f_out.write(i)
f_in.close()
f_out.close()