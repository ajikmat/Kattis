correct = [1, 1, 2, 2, 2, 8]
got = []

a, b, c, d, e, f = map(int, input().split())

got.append(a)
got.append(b)
got.append(c)
got.append(d)
got.append(e)
got.append(f)


diff = []
for i in range(6):
    diff.append(correct[i] - got[i])
    
print(*diff, sep = " ")
