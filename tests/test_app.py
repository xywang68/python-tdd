import pytest

from app.app import hello

def test_app():
    assert hello() == "Hello, Blackjack!"
