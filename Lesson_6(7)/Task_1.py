class CustomList(object):

    def __init__(self, *args):
        self.my_custom_list = [*args]
        self.item = args

    def __setitem__(self, index, value):
        self.my_custom_list[index] = value

    def __getitem__(self, index):
        return self.my_custom_list[index]

    def __str__(self):
        return str(self.my_custom_list)

    def __add__(self, other):
        return CustomList(*self.item, *other.item)

    def clear(self):
        self.my_custom_list = []
        return self.my_custom_list

    def remove(self, element):
        if element in self.my_custom_list:
            for index, item in enumerate(self.my_custom_list):
                if item == element:
                    self.my_custom_list = self.my_custom_list[:index] + self.my_custom_list[index + 1:]
                    break
            return self.my_custom_list
        else:
            raise ValueError(f'<<{element}>> not in list')

    def pop(self, index=None):
        if index is None:
            pop_item = self.my_custom_list[-1]
            self.my_custom_list = self.my_custom_list[:-1]
            return pop_item
        elif 0 <= index <= (len(self.my_custom_list) - 1):
            pop_item = self.my_custom_list[index]
            self.my_custom_list = self.my_custom_list[:index] + self.my_custom_list[index + 1:]
            return pop_item
        elif (1 - len(self.my_custom_list)) <= index < 0:
            pop_item = self.my_custom_list[index]
            self.my_custom_list = self.my_custom_list[:len(self.my_custom_list) + index] + \
                                  self.my_custom_list[len(self.my_custom_list) + index + 1:]
            return pop_item
        else:
            raise IndexError(f'pop index out of range')

    def append(self, element):
        self.my_custom_list = self.my_custom_list + [element]
        return self.my_custom_list

    def insert(self, index, element):
        self.my_custom_list = self.my_custom_list[:index] + [element] + self.my_custom_list[index:]
        return self.my_custom_list
