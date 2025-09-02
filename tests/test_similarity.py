# test_similarity.py - Simple test cases

from src.similarity import check_similarity

def test_similarity():
    assert check_similarity("Daily Times", "The Daily Times") > 80
