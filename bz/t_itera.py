a=[x*2 for x in range(5)]
print(a)
b=(x*2 for x in range(5))
print(b)
b=tuple(b)
print(b)
c=(x for x in  range(3))
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())

