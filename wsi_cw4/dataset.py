from random import randrange, shuffle

class Dataset:
    def __init__(self, filename):
        self.data = None
        self.attribute_list = None
        self.attribute_count = None
        self.training_set = None
        self.training_size = None
        self.test_set = None
        self.test_size = None
        self.readFromFile(filename)
        self.divideDataset()
        self.createAtributeSets()

    def readFromFile(self, filename):
        self.data = []
        f = open(filename, "r")
        text = f.read()
        if text == "":
            raise(Exception)
        rows = text.split('\n')
        if rows[-1] == '':
            rows.pop()
        shuffle(rows)
        for row in rows:
            self.data.append(row.split(","))
        self.size = len(self.data)
        self.attribute_count = len(self.data[0])

    def createAtributeSets(self):
        self.attribute_list = []
        for i in range(self.attribute_count):
            newset = set()
            for elem in self.data:
                newset.add(elem[i])
            self.attribute_list.append(newset)

    def divideDataset(self):
        self.training_set = []
        self.test_set = []
        start = randrange(0, self.size)
        stop = start + (self.size * 2) // 5
        if stop > self.size - 1:
            stop = start - (self.size * 3) // 5
        current = start
        while (current != stop):
            self.test_set.append(self.data[current])
            current += 1
            if current == self.size:
                current = 0
        while (current != start):
            self.training_set.append(self.data[current])
            current += 1
            if current == self.size:
                current = 0
        self.training_size = len(self.training_set)
        self.test_size = len(self.test_set)

# d = Dataset("agaricus-lepiota.data")
# d = Dataset("datatest.data")
# pass

