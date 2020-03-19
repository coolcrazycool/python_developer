from array import array


class Arr:
    def __init__(self, element_type, *elements):
        self.el_type = element_type
        self.data = array(element_type, elements)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.data[item]
        else:
            return self.data[item]

    def __delitem__(self, key):
        del self.data[key]

    def __setitem__(self, key, value):
        for i in range(len(self.data)):
            if self.data[i] == key:
                self.data[i] = value

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        for i in range(len(self.data)):
            if self.data[i] == item:
                return True
            return False

    def __iter__(self):
        return Iterator(self.data)

    def __reversed__(self):
        return Iterator(self.data, -1)

    def index(self, item):
        for i in range(len(self.data)):
            if self.data[i] == item:
                return i
        return -1

    def count(self, item):
        counter = 0
        for i in range(len(self.data)):
            if self.data[i] == item:
                counter += 1
        return counter

    def insert(self, position, item):
        sec_array = [_ for _ in self.data[position::]]
        second_part = Arr(self.rtype, *sec_array)
        fir_array = [_ for _ in self.data[:position:]]
        first_part = Arr(self.rtype, *fir_array)
        new_array = Arr(self.rtype, *first_part, *item, *second_part)
        self.data = new_array

    @property
    def rtype(self):
        return self.el_type

    def append(self, item):
        new_array = Arr(self.rtype, *self.data, item)
        self.data = new_array

    def extend(self, item):
        new_array = Arr(self.rtype, *self.data, *item)
        self.data = new_array

    def clear(self):
        for i in range(len(self.data) - 1, -1, -1):
            del self.data[i]

    def pop(self, item):
        last = self.data[item]
        del self.data[item]
        return last

    def remove(self, item):
        del self.data[item]

    def isEmpty(self):
        return self.data == []


class Iterator:
    def __iter__(self):
        return self

    def __init__(self, collection, cursor=1):
        self.collection = collection
        self.cursor = cursor
        if cursor == 1:
            self._cursor = -1
            self.step = 1
        if cursor == -1:
            self._cursor = len(self.collection)
            self.step = -1

    def __next__(self):
        self._cursor += self.step
        if self._cursor < 0 or self._cursor >= len(self.collection):
            raise StopIteration()
        return self.collection[self._cursor]
