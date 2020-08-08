

class DynamicArray:
    def __init__(self, maximum=1):
        # create dynamic array
        self.list = [0] * maximum
        self.allocationSize = maximum
        self.curr_size = 0

    def resize(self, newAllocationSize):
        for i in range(newAllocationSize - len(self.list)):
            self.list.append(0)
        self.allocationSize = newAllocationSize

    def append(self, newItem):
        if self.allocationSize == self.curr_size:
            self.resize(len(self.list) * 2)
        self.list[self.curr_size] = newItem
        self.curr_size += 1

    def prepend(self, newItem):
        if self.allocationSize == self.curr_size:
            self.resize(len(self.list) * 2)
        # inserting newItem at [0]
        last_val = self.list[self.curr_size - 1]
        for i in range(self.curr_size - 1, 0, -1):
            self.list[i] = self.list[i - 1]
        self.list[0] = newItem
        self.insert_after(self.curr_size - 1, last_val)
        self.curr_size += 1

    def insert_after(self, index, newItem):
        if self.allocationSize == self.curr_size:
            self.resize(len(self.list) * 2)
        if index + 1 < len(self.list):
            self.list[index + 1] = newItem
            self.curr_size += 1
        else:
            print('Index out of bounds in InsertAfter, skipping')

    def search(self, item):
        for i in range(len(self.list)):
            if self.list[i] == item:
                return i
        return -1

    def remove_at(self, index):
        if 0 <= index < len(self.list):
            for i in range(len(self.list) - 1):
                self.list[i] = self.list[i + 1]
            self.curr_size -= 1

    def sort(self, key=None):
        if key:
            self.list = sorted((x for x in self.list if x != 0), key=key)
        else:
            self.list = sorted(self.list)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, item):
        return self.list[item]

    def __setitem__(self, key, value):
        self.list[key] = value

    def __iter__(self):
        return (x for x in self.list if x != 0)

