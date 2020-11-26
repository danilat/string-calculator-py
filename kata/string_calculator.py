from typing import Tuple, List

class StringCalculator:
    def __parse_numbers(self, numbers: str) -> Tuple[str, str]:
        values = numbers
        separator = ","

        if numbers.startswith("//"):
            separator = numbers[2]
            values = numbers[4:]
            
        return separator, values

    def __assert_no_negative_numbers(self, tokens: List[int]) -> None:
        negative_numbers = [x for x in tokens if x < 0]
        if negative_numbers:
            raise NoNegativeNumbersAllowedError(negative_numbers)

    def add(self, numbers: str) -> int:        
        if not numbers:
            return 0
            
        separator, values = self.__parse_numbers(numbers)

        tokens = [int(x) for x in values
        .replace("\n", separator)
        .split(separator)]

        self.__assert_no_negative_numbers(tokens)

        tokens = [x for x in tokens if x < 1000]

        return sum(tokens)            

class NoNegativeNumbersAllowedError(Exception):
    def __init__(self, negative_numbers:List[int]): 
        negative_numbers_str = ",".join(map(str, negative_numbers))   
        super().__init__(f"Negatives not allowed {negative_numbers_str}")