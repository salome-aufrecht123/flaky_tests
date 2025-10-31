import pytest
import random

def test_flaky_example():
    assert random.choice([True, False]) or random.choice([True, False])  # Zufällig erfolgreich/scheiternd

def test_always_passes():
    assert True