class DinamicArray:
    @staticmethod
    def checkValidity(capacity , arr: list):
        try:
            if capacity < 1:
                raise Exception("The capacity must be greater than 0")
            if len(arr) < 1:
                raise Exception("The array is not yet initialized")
            print(capacity > 1)
        except Exception as e:
            print(f"Error: {e}")

    def __init__(self, capacity: int):
        if capacity < 1:
            raise Exception("Capacity must be greater than 0")
        self.capacity = capacity

        #initialize array with the capacity
        self.ar = [0] * capacity

    def printMe(self):
        array_length = len(self.ar)
        print(f"Capacity is {self.capacity} and array length is  {array_length}, array: {self.ar}")

    def get(self, i: int):
        try:
            if len(self.ar) < 1:
                raise Exception("Array is not initialized")
            return self.ar[i]
        except Exception as e:
            print(f"Erorr: {e}")

    # def pushRandom(self):
    #     for r in range(self.capacity):
    #         random_value = random.randrange(0, self.capacity)
    #         self.ar[r] = random_value
obj = DinamicArray(3)
# obj.pushRandom()
obj.printMe()
print(obj.get(1))
