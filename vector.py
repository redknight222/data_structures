import string


class vector:

    def __init__(self):
        self.my_array = ['' for _ in range(10)]
        self.size = 0

    def add_element(self, element):
        self.my_array[self.size] = element
        self.size += 1

    def debug_print(self):
        for i in range(self.size + 1):
            print(self.my_array[i])

    def debug_array(self):
        return self.my_array[0:self.size]

    def remove_element(self):
        self.remove_object = input("Введите элемент или его номер(>0), чтобы удалить ")
        if self.remove_object in self.my_array:
            self.my_array.remove(self.remove_object)
        elif self.remove_object in string.digits and 0 <= int(self.remove_object) <= self.size:
            self.my_array.pop(int(self.remove_object) - 1)
        else:
            print("Ошибка.Такого элемента(или номера) не существует")
