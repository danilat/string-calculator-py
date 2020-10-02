import pytest

from kata.string_calculator import StringCalculator
from kata.kata_error import KataError

def test_empty_string():
    string_calculator = StringCalculator()

    result = string_calculator.add("")

    assert result == 0

def test_when_one_number_with_value_1_returns_number():
    string_calculator = StringCalculator()

    result = string_calculator.add("1")

    assert result == 1

def test_when_one_number_with_value_17_returns_number():
    string_calculator = StringCalculator()

    result = string_calculator.add("17")

    assert result == 17

def test_when_two_numbers_returns_the_sum():
    string_calculator = StringCalculator()

    result = string_calculator.add("1,8")

    assert result == 9

def test_when_more_than_two_numbers_returns_the_sum():
    string_calculator = StringCalculator()

    result = string_calculator.add("1,8,34")

    assert result == 43

def test_when_more_than_two_numers_with_newline_retrns_the_shum():
    string_calculator = StringCalculator()

    result = string_calculator.add("1,8\n34")

    assert result == 43

def test_the_sum_of_the_numbers_custom_delimiter():
    string_calculator = StringCalculator()

    result = string_calculator.add("//;\n1;2")

    assert result == 3

def test_when_negative_numbers_raise_error():
    string_calculator = StringCalculator()

    with pytest.raises(KataError):
        string_calculator.add("-1")


def greeting(name: str) -> str:
  return 'Hello ' + name

greeting(1)