class Par:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.index:
            raise StopIteration
        result = (self.data[self.n])
        self.n += 2
        return result
            
        

imie = Par("parzyste")
print(imie)
for x in imie:
    print(x)

