from src.unicode_strings import equal_ignores_case


def test_equal_ignores_case():
    assert equal_ignores_case('el aguacate', 'El aguacate') is True
    assert equal_ignores_case('Die Straße', 'die Strasse') is True
