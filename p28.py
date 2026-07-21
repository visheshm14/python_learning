class emp:
    a=1

class programmer(emp):
    b=2

class manager(programmer):
    c=3

o= emp()
print(o.a)

o= programmer()
print(o.a,o.b)

o= manager()
print(o.a,o.b,o.c)