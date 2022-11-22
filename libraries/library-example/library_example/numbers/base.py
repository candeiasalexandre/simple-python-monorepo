from typing import Union


class Number:
    def __init__(self, number: Union[int, float]) -> None:
        self._number = number

    def __add__(self, other: "Number") -> "Number":
        return Number(self._number + other._number)

    def __str__(self) -> str:
        return str(self._number)


def number_from_int(number: int) -> Number:
    return Number(number)
