__author__ = 'Aidan'

m = [2,4,6,8]
print(m[1])
fivem = []
for i in range(len(m)):
    fivem.append(m[i]*5)
print(fivem)
m.append(10)
print(m)
m.append(6)
print(m)
print(m.index(8))
m.remove(m[3])
print(m)