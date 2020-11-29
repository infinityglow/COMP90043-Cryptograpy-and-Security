import numpy as np

dig2char = {}
char2dig = {}

for i in range(65, 91):
    dig2char[i-65] = chr(i)
for j in range(48, 58):
    dig2char[j-22] = chr(j)
dig2char[36] = chr(32)

for k, v in dig2char.items():
    char2dig[v] = k

key_inv = np.array([[31,  6,  8, 14, 32],
                    [30, 10, 28, 31, 15],
                    [ 3, 19, 31, 15,  5],
                    [ 1, 19,  7, 13,  7],
                    [12, 31, 11, 14, 26]])

c = "A8VS3XRDEON6JEVXGJID13C07L4C1R4Q965XWRA5DQGYWTNHYO4ND8Z"
p = ""
for k in range(11):
    c_piece = c[k*5: (k+1)*5]
    c_dig = np.zeros([1, 5])
    for i in range(5):
        c_dig[0][i] = char2dig[c_piece[i]]
    p_dig = np.dot(key_inv, c_dig.T) % 37
    for j in range(5):
        p += dig2char[p_dig[j][0]]
print(p)

p = 'X9B6T6JAW3UEY7FHIW581705Z'
ptxt = []; row = []
for i in range(len(p)):
    row.append(char2dig[p[i]])
    if i % 5 == 4:
        ptxt.append(row)
        row = []

d = '2Q59ZZ1Z58170UMDNY2JHINTS'
dtxt = []; row = []
for i in range(len(d)):
    row.append(char2dig[d[i]])
    if i % 5 == 4:
        dtxt.append(row)
        row = []

