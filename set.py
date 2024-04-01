user_id = {11,11,22,33}
print(user_id)

a = {1,2,3,4,5}
a.add(6)
a.add('Nepal')
print(a)
a.remove(5)
print(a)
b = a.copy()
print(b)
b.clear()
print(b)

#differnce
A = {'a', 'b', 'c', 'd', 'e'}
B = {'f', 'g', 'h', 'i', 'j', 'b'}
print(A.difference(B))
print(A.intersection(B))
print(A.isdisjoint(B))
print(A.issubset(B))
print(A.symmetric_difference(B))
print(A.union(B))


re = a.pop()
print(re)
y = {'a', 'b', 'c', 'd'}
rel = y.pop()
print(rel)
