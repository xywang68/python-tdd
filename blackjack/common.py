def card_score(cards):

    if type(cards) is not str:
        raise TypeError("cards should be of string type, got: cards: {}, type: {}", cards, type(cards))

    if len(cards) < 2:
        raise ValueError("cards should have at least 2 cards, got: cards: {}, len: {}", cards, len(cards))

    valid_cards = "23456789XJQKA"
    if len([b for b in cards if b not in valid_cards]):
        raise ValueError("cards should be in valid range {}, got {}", valid_cards, cards)

    numbers = [c for c in cards if c in "23456789"]
    faces = [c for c in cards if c in "XJQK"]
    n_aces = sum([1 for c in cards if c == "A"])
    score = sum([int(i) for i in numbers]) + len(faces) * 10

    while n_aces > 0:
        if (score + n_aces * 11) > 21:
            score += 1
        else:
            score += 11
        n_aces -= 1

    return score if score <= 21 else 0

