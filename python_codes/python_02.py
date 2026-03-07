class Test:

    def __init__(self,age):
        self._age = age
    
    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self,age):
        if 10 < age < 100:
            self._age = age
        else:
            print("value error")

t = Test(20)
print(t.age)