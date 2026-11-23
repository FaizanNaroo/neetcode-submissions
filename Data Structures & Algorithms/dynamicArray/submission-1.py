class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0] * capacity
        self.count = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.count == self.capacity:
            self.resize()

        self.array[self.count] = n
        self.count += 1

    def popback(self) -> int:
        self.count -= 1
        return self.array[self.count]

    def resize(self) -> None:
        new_capacity = 2 * self.capacity
        new_array = [0] * new_capacity

        for i in range(self.count):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.count

    def getCapacity(self) -> int:
        return self.capacity