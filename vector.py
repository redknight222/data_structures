class vector():

    def __init__(self):
        self.my_array = ['' for i in range(10)]
        self.size = 0

    def add_element(self,element):
        self.my_array[self.size] = element
        self.size += 1

    def debug_print(self):
        for i in range(self.size + 1):
            print(self.my_array[i])

    def debug_array(self):
        return self.my_array[0:self.size]

#    def remove_element(self):

