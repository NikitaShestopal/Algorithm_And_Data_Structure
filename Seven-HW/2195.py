import re

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
    N, M = map(int, input().split())

    vocabHT = HashTable()
    usedHT = HashTable()

    for _ in range(N):
        word = input().strip().lower()
        vocabHT.put(word, True)
        usedHT.put(word, False)

    text_lines = []
    for _ in range(M):
        text_lines.append(input())
    text = '\n'.join(text_lines)

    words_in_text = re.findall(r"[A-Za-z]+", text)
    words_in_text = [w.lower() for w in words_in_text]

    unknown_found = False

    for w in words_in_text:
        if vocabHT.get(w) is None:
            unknown_found = True
            break
        else:
            usedHT.put(w, True)

    if unknown_found:
        print("Some words from the text are unknown.")
        return

    all_used = True
    for key, val in zip(vocabHT.keys, vocabHT.values):
        if key is not None:
            if usedHT.get(key) != True:
                all_used = False
                break

    if not all_used:
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")


if __name__ == '__main__':
    main()