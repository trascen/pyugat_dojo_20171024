import pytest

from bowler import score

@pytest.mark.parametrize('test, expected', [
        ('0'*20, 0),
        ('X'*12, 300),
        ('90'*10, 90),
        ('5/'*10 + '5', 150),
        ])
def test_score(test, expected):
    assert score(test) == expected

@pytest.mark.parametrize('test', [
    'X', 'x', 'd', '444'
    ])
def test_invalid(test):
    with pytest.raises(ValueError):
        score(test)

