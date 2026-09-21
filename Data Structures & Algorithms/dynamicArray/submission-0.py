class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.current_capcity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.current_capcity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        val = self.arr[self.length - 1]
        self.length -= 1
        return val
 

    def resize(self) -> None:
        self.current_capcity *= 2
        tmp = [0] * self.current_capcity

        for i in range(self.length):
            tmp[i] = self.arr[i] 
        
        self.arr = tmp




    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.current_capcity
