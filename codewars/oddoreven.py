import numpy as np


def odd_or_even(arr):
    sum = 0
    result = ""
    new_array = np.array(arr)
    if new_array.size == 0:
        new_array = np.zeros((1,), dtype=int)
    for number in new_array:
        sum += number
    result = "even" if sum % 2 == 0 else "odd"

    return result


print(odd_or_even([0, -1, -5]))
