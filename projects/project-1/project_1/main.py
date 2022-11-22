from library_example.utils import multiply_5
from library_example.numbers.base import number_from_int

from library_example.numbers.numpy_utils import create_zeros_array
from library_example.numbers.numpy_utils import create_ones_array


def main() -> None:
    print(multiply_5(10))

    number_1 = number_from_int(10)
    number_2 = number_from_int(20)

    print(number_1 + number_2)


if __name__ == "__main__":
    main()
