class a:
    label = "a"

class b(a):
    label = "b"

class c(a):
    label = "c"

class d(c,b):
    pass

cup = d()
print(cup.label)
print(d.__mro__)