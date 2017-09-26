class Deck:
    def __init__(self):
        self.cards = []
        for p in ['Spades', 'Diamonds', 'Hearts', 'Clubs']:
            for n in range(1, 14):
                self.cartas.append(Card(n, p))

    def __iter__(self):
        return iter(self.cards)


for c in Deck():
    print(c)
