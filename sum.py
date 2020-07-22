

import functools
def sum_1(my_list):
    return functools.reduce(lambda a, b: a+ b, [sub[1] for sub in my_list])

def sum_2(my_list):
    return functools.reduce(lambda a, b: a + b[1], my_list, 0)

import numpy as np
def sum_3(my_list):
    my_array = np.array(my_list)
    np.sum(my_array[:, 1])

import operator
def sum_4(my_list):
    return functools.reduce(operator.add, [sub[1] for sub in my_list], 0)

def sum_5(my_list):
    t = 0
    for sub in my_list:
        t += sub[1]
    return t

def sum_6(my_list):
    return sum([sub[1] for sub in my_list])
def sum_7(my_list):
    return sum(sub[1] for sub in my_list)


from timeit import default_timer as timer
from datetime import timedelta
def time_it(func, values):
    # time a function
    start = timer()
    print(func.__name__)
    print(func(values))
    end = timer()
    print(timedelta(seconds=end-start))

if __name__ == '__main__':
   # my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
   # time_it(sum_1, my_list)
   # time_it(sum_2, my_list)
   # time_it(sum_3, my_list)
   # time_it(sum_4, my_list)
   # time_it(sum_5, my_list)
   # time_it(sum_6, my_list)

    for i in range(1, 7):
        my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
        time_it(eval(f'sum_{i}'), my_list)
