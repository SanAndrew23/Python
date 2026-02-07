d = dict()
lst = list(map(str, input().split()))
count = 1
for i in lst:
    if i not in d:
        d[i] = count
    else:
        d[i] = (count + 1)
m_word = ''
m_count = 0
for word, count in d.items():
    if count > m_count:
        m_word = word
        m_count = count
    elif count == m_count:
        if word[0] < m_word[0]:
            m_word = word
            m_count = count
print(m_word)