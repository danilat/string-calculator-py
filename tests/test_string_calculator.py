import pytest
from kata.string_calculator import StringCalculator, NoNegativeNumbersAllowedError 

@pytest.fixture
def string_calculator():
    return StringCalculator()

def test_empty_string(string_calculator):
    result = string_calculator.add("")

    assert result == 0

def test_only_one_value(string_calculator):
    result = string_calculator.add("1")

    assert result == 1

def test_only_two_values(string_calculator):
    result = string_calculator.add("1,2")

    assert result == 3

def test_unknown_values(string_calculator):
    result = string_calculator.add("1,2,3,5,7,288")

    assert result == 306

def test_new_line_separator(string_calculator):
    result = string_calculator.add("1\n2,3,5,7,288")

    assert result == 306

def test_custom_delimiter_separator(string_calculator):
    result = string_calculator.add("//;\n1;2")

    assert result == 3

def test_multiple_negative_numbers_throws_exception(string_calculator):    
    with pytest.raises(NoNegativeNumbersAllowedError) as excinfo:
        result = string_calculator.add("-1,2,-3")
    assert "Negatives not allowed -1,-3" == str(excinfo.value)

def test_avoid_numbers_bigger_than_1000(string_calculator):
    result = string_calculator.add("2,1000")

    assert result == 2