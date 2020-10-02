from .kata_error import KataError

class StringCalculator:
    def add(self, numbers):
        if numbers == '':
            return 0

        if numbers.startswith('//'):
            delimiter = numbers[2]
            numbers = numbers[4:].replace(delimiter, ",")
        else:
            numbers = numbers.replace("\n", ",")

        sum_ = 0
        for number in numbers.split(','):
            integer = int(number)
            if integer < 0:
                raise KataError
            
            sum_ += integer

        return sum_



