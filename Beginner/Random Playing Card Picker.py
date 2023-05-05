
import random


def random_playingcard(cards: list, ranks: list) -> str:
    card = random.choice(cards)
    rank = random.choice(ranks)
    return f"The {rank} of {card}"

cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

randomCard = random_playingcard(cards, ranks)

print(randomCard)
