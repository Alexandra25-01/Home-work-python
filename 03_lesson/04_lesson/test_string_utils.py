import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("str_whitespace, expected", [
    ("   How are you", "How are you"),
    ("   Привет", "Привет"),
    ("     test", "test"),
])
def test_trim_positive(str_whitespace, expected):
    assert string_utils.trim(str_whitespace) == expected


@pytest.mark.negative
@pytest.mark.parametrize("str_whitespace, expected", [
    ("test", "test"),
    ("   !><", "!><"),
    ("   Hello   ", "Hello   "),
    ("    ", ""),
    ("", ""),
    ("  python pytnon", "python pytnon")
])
def test_trim_negative(str_whitespace, expected):
    assert string_utils.trim(str_whitespace) == expected


@pytest.mark.positive
@pytest.mark.parametrize("str, symbol, expected", [
    ("SkyPro", "S", True),
    ("Привет", "т", True),
    ("Python", "t", True),
    ("P", "P", True),
    ("bbbb", "b", True),
])
def test_contains_positive(str, symbol, expected):
    assert string_utils.contains(str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("str, symbol, expected", [
    ("Python", "b", False),
    ("", "b", False),
    ("     ", "b", False),
    ("bbbb", " ", False),
    ("1323234", "a", False),
])
def test_contains_negative(str, symbol, expected):
    assert string_utils.contains(str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("str, symbol, expected", [
    ("Hello", "o", "Hell"),
    ("Pytest", "P", "ytest"),
    ("Python", "t", "Pyhon"),
    ("Hello world", " ", "Helloworld"),
    ("positive test", "i", "postve test"),
    ("home work lesso4", "home work lesso4", ""),
    ("16577", "5", "1677"),
    ("<>?!@,.", "?", "<>!@,."),
])
def test_delete_symbol_positive(str, symbol, expected):
    assert string_utils.delete_symbol(str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("str, symbol, expected", [
    ("Pytest", "W", "Pytest"),
    ("", "d", ""),
    ("fgfhfhg", "", "fgfhfhg"),
    ("", "  ", ""),
    ("    ", "    ", ""),
])
def test_delete_symbol_negative(str, symbol, expected):
    assert string_utils.delete_symbol(str, symbol) == expected
