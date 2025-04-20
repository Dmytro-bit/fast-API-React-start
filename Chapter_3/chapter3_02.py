from typing import List, Literal


def square_numbers(numbers: List[int]) -> List[int]:
    return [number ** 2 for number in numbers]


input_numbers: list[int] = [1, 2, 3, 4, 5]

squared_numbers = square_numbers(input_numbers)
account_type: Literal["personal", "business"]
account_type = "personal"


print(squared_numbers)
