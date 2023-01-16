import pytest

from blackjack.common import card_score

# test two cards positive
@pytest.mark.parametrize("cards, score", [
    ("JK", 20),
    ("78", 15),
    ("7K", 17),
    ("JA", 21),
    ("XX", 20),
    ("AA", 12)
    ])
def test_two_cards(cards, score):
    assert card_score(cards) == score

# test more cards positive
@pytest.mark.parametrize("cards, score", [
    ("JKA", 21),
    ("78X", 0),
    ("7KAAA", 20),
    ("JAA", 12),
    ("XX2", 0),
    ("AAAA", 14)
    ])
def test_more_cards(cards, score):
    assert card_score   (cards) == score

# test rasie error if cards type is wrong
@pytest.mark.parametrize("cards", [
    (12),
    (["A"])
    ])
def test_raise_type_error_if_cards_type_is_wrong(cards):
    assert type(cards) != str
    with pytest.raises(TypeError):
        card_score(cards)

# test raise error if less than two cards
@pytest.mark.parametrize("cards", [
    ("X"),
    ("2")
    ])
def test_raise_value_error_if_cards_has_only_1_card(cards):
    assert len(cards) == 1
    with pytest.raises(ValueError):
        card_score(cards)

# test raise error of cards contain invalid card
@pytest.mark.parametrize("cards", [
    ("2A1"),
    ("10")
    ])
def test_raise_value_error_if_cards_contains_wrong_card(cards):
    assert len(cards) >= 2
    with pytest.raises(ValueError):
        card_score(cards)