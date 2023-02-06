import pytest

from blackjack.common import return_valid_cards
from blackjack.common import return_valid_suits
from blackjack.common import card_score

# test return_valid_cards returns the expected cards
my_valid_cards_for_test = "23456789XJQKA"
@pytest.mark.parametrize("test_cards", [
    pytest.param("", marks=pytest.mark.xfail),
    my_valid_cards_for_test
])
def test_return_valid_cards(test_cards):
    return_value = return_valid_cards()
    assert type(return_value) == str 
    assert return_value == test_cards

# test return_valid_suits returns the expected suits
my_valid_suits_for_test = "CDHS"
@pytest.mark.parametrize("test_suits", [
    pytest.param("", marks=pytest.mark.xfail),
    my_valid_suits_for_test
])
def test_return_valid_suits(test_suits):
    return_value = return_valid_suits()
    assert type(return_value) == str 
    assert return_value == test_suits

# test two cards positive
@pytest.mark.parametrize("cards, score", [
    # xfail test to proof the test_two_cards() function can catch expected failure
    pytest.param("23", 0, marks=pytest.mark.xfail),
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
    # xfail test to proof the test_more_cards() function can catch expected failure
    pytest.param("234", 0, marks=pytest.mark.xfail),
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
    pytest.param("234", marks=pytest.mark.xfail),
    (12),
    (["A"])
    ])
def test_raise_type_error_if_cards_type_is_wrong(cards):
    assert type(cards) != str
    with pytest.raises(TypeError):
        card_score(cards)

# test raise error if less than two cards
@pytest.mark.parametrize("cards", [
    pytest.param("22", marks=pytest.mark.xfail),
    ("X"),
    ("2")
    ])
def test_raise_value_error_if_cards_has_only_1_card(cards):
    assert len(cards) == 1
    with pytest.raises(ValueError):
        card_score(cards)

# test raise error of cards contain invalid card
@pytest.mark.parametrize("cards", [
    pytest.param("22", marks=pytest.mark.xfail),
    ("2A1"),
    ("10")
    ])
def test_raise_value_error_if_cards_contains_wrong_card(cards):
    assert len(cards) >= 2
    with pytest.raises(ValueError):
        card_score(cards)
