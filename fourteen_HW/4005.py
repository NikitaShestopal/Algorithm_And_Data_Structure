class Queue:
    def __init__(self, maxsize=100):
        self._items = [None for _ in range(maxsize)]
        self._front = 0
        self._back = 0
        self._size = 0

    def push(self, item):
        if self._size > 0:
            self._back = (self._back + 1) % len(self._items)
        self._items[self._back] = item
        self._size += 1
        return "ok"

    def pop(self):
        if self._size == 0:
            return None
        item = self._items[self._front]
        self._size -= 1
        if self._size > 0:
            self._front = (self._front + 1) % len(self._items)
        return item

    def front(self):
        if self._size == 0:
            return None
        return self._items[self._front]

    def size(self):
        return self._size


def compare_cards(card1, card2, n):
    if card1 == 0 and card2 == n - 1:
        return "first"
    if card2 == 0 and card1 == n - 1:
        return "second"
    if card1 > card2:
        return "first"
    return "second"


def solve():
    n = int(input().strip())
    deck1_cards = list(map(int, input().split()))
    deck2_cards = list(map(int, input().split()))

    deck1 = Queue(maxsize=n + 5)
    deck2 = Queue(maxsize=n + 5)

    for card in deck1_cards:
        deck1.push(card)
    for card in deck2_cards:
        deck2.push(card)

    moves = 0
    max_moves = 200000

    while deck1.size() > 0 and deck2.size() > 0 and moves < max_moves:
        moves += 1
        card1 = deck1.pop()
        card2 = deck2.pop()
        winner = compare_cards(card1, card2, n)

        if winner == "first":
            deck1.push(card1)
            deck1.push(card2)
        else:
            deck2.push(card1)
            deck2.push(card2)

    if moves >= max_moves:
        print("draw")
    else:
        if deck1.size() == 0:
            print("second", moves)
        else:
            print("first", moves)


if __name__ == '__main__':
    solve()
