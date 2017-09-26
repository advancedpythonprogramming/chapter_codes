class Card:
    FACE_CARDS = {11: 'J', 12: 'Q', 13: 'K'}

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value if value <= 10 else Card.FACE_CARDS[value]

    def __str__(self):
        return "%s %s" % (self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        for s in ['Spades', 'Diamonds', 'Hearts', 'Clubs']:
            for v in range(1, 14):
                self.cards.append(Card(v, s))


for c in Deck().cards:
    print(c)
