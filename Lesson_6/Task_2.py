class CustomDict(object):

    def __init__(self, **kwargs, ):
        self.item = kwargs
        self.my_custom_dict = {**self.item}

    def __setitem__(self, key, value):
        self.my_custom_dict[key] = value

    def __getitem__(self, key):
        return self.my_custom_dict[key]

    def __str__(self):
        return str(self.my_custom_dict)

    def __add__(self, other):
        for i in self.item:
            if i in other.item:
                raise TypeError(f'Multiple values for keyword argument <<{i}>>')
            else:
                return CustomDict(**self.item, **other.item)

    def get(self, key):
        if key in self.my_custom_dict:
            return self.my_custom_dict[key]

    def items(self):
        items_list = []
        for key in self.my_custom_dict:
            items_list.append((key, self.my_custom_dict[key]))
        return items_list

    def keys(self):
        keys_list = []
        for key in self.my_custom_dict:
            keys_list.append(key)
        return keys_list

    def values(self):
        values_list = []
        for key in self.my_custom_dict:
            values_list.append(self.my_custom_dict[key])
        return values_list
