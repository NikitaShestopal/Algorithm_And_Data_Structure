class HashTable:
    def __init__(self):
        self.size = 1000003
        self.currentSize = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        current = self.hash(key)
        while self.keys[current] is not None:
            if self.keys[current] == key:
                self.values[current] = value
                return
            current = (current + 1) % self.size

        self.keys[current] = key
        self.values[current] = value
        self.currentSize += 1

    def get(self, key):
        current = self.hash(key)
        while self.keys[current] is not None:
            if self.keys[current] == key:
                return self.values[current]
            current = (current + 1) % self.size
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

def main():
    N = int(input())  
    numbers = input().split()  

    unique_numbers = HashTable()

    for number in numbers:
        unique_numbers.put(number, True)

    count = 0
    for key, value in zip(unique_numbers.keys, unique_numbers.values):
        if key is not None:
            count += 1

    print(count)

if __name__ == '__main__':
    main()