from src.unicode_strings import equal_ignores_case


def test_join_strings():
    assert equal_ignores_case('die Straße', 'die Strasse') is True
