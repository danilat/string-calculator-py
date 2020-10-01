def test_empty_string():
    string_calculator = StringCalculator()
    
    result = string_calculator.add("")

    assert result == 0