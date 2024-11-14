class House:
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number = number_of_floors

    def go_to(self, new_floor):

        if int(new_floor) < 1 or int(new_floor) > int(self.number):
            print("Такого этажа не существует")
        else:
            i = 1
            while i <= int(new_floor):
                print(i)
                i += 1
    def __len__(self):
        return self.number
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number}"
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number==other.number
        elif  isinstance(other, int):
            return self.number == other
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number < other.number
        elif isinstance(other, int):
            return self.number < other
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
    def __gt__(self, other):
        return not self.__le__(other)
    def __ge__(self, other):
        return not self.__lt__(other)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __add__(self, other):
        if isinstance(other, int):
            self.number += other
        elif isinstance(other, House):
            self.number += other.number
        return self
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1.__add__(10) # __add__
print(h1)
print(h1 == h2)
h1.__iadd__(10) # __iadd__
print(h1)
h2.__radd__(10) # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
