from sys import stdin

d = dict()
lst = list(map(str, stdin.read().split()))
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# Короткое решение через сортировку с параметрами
'''print(sorted(d.items(), key=lambda x: (-x[1], x[0]), reverse=True)[-1][0])'''

m_word = ''
m_count = 0
for word, count in d.items():
    if count > m_count:
        m_word = word
        m_count = count
    elif count == m_count:
        if word < m_word:
            m_word = word
            m_count = count
print(m_word)

