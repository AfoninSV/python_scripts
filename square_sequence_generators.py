"""
This module generates a sequence of squares of numbers from 1 to N 
using different methods: iterator class, generator function, and generator expression.
"""

from math import pow


class PowIter:
    """
    Iter class
    Returns power of 2 from every number till limit

    :rtype: int
    """

    def __init__(self, peak: int):
        self.peak = peak
        self.counter = 1

    def __iter__(self):
        self.counter = 1
        return self

    def __next__(self):
        if self.counter >= self.peak:
            raise StopIteration
        pow_num = pow(self.counter, 2)
        self.counter += 1
        return pow_num


def pow_generator(peak: int):
    for num in range(1, peak):
        yield pow(num, 2)


def pow_expression(peak: int):
    return (pow(num, 2) for num in range(1, peak))


def print_examples(cls, func, exp):
    """Outputs objects themselves and as list"""
    print(cls, list(cls))
    print(func, list(func))
    print(exp, list(exp))


peak_number = int(input('Введите число: '))

class_iter = PowIter(peak_number)
func_generator = pow_generator(peak_number)
gen_expression = pow_expression(peak_number)
print_examples(class_iter,
               func_generator,
               gen_expression)
