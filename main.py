import random
import timeit

import matplotlib.pyplot as plt
import numpy as np

from sorters.bubble import bubble_sort
from sorters.fractal_basic import fractal_sort
from sorters.fractal_optimised import fractal_optim
from sorters.insert import insert_sort
from visualizer import valuelabel

if __name__ == '__main__':
    ints = [random.randint(0, 100) for _ in range(10000)]

    ITERS = 10

    bubble_time = timeit.timeit(lambda: bubble_sort(ints.copy()), number=ITERS)
    insert_time = timeit.timeit(lambda: insert_sort(ints.copy()), number=ITERS)
    fractal_time = timeit.timeit(lambda: fractal_sort(ints.copy()), number=ITERS)
    optim_fractal_time = timeit.timeit(lambda: fractal_optim(ints.copy()), number=ITERS)

    performance = [bubble_time, insert_time, fractal_time, optim_fractal_time]
    objects = ('bubble sort', 'insert sort', 'fractal sort', 'optimised fractal sort')

    valuelabel(objects, performance)

    y_pos = np.arange(len(objects))

    plt.bar(y_pos, performance, align='center', color='orange')
    plt.xticks(y_pos, objects)
    plt.ylabel('performance time (seconds)')
    plt.title('Производительность различных алгоритмов сортировки')

    plt.show()
