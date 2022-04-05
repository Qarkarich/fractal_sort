import datetime
import random

from sorters.bubble import bubble_sort
from sorters.fractal_optimised import fractal_sort
from sorters.insert import insert_sort

if __name__ == '__main__':
    ints = [random.randint(0, 100) for _ in range(1000)]

    start = datetime.datetime.now().microsecond
    bubble_sort(ints)
    end = datetime.datetime.now().microsecond

    print(f'bubble sort: {end - start} ms')

    ints = [random.randint(0, 100) for _ in range(1000)]

    start = datetime.datetime.now().microsecond
    insert_sort(ints)
    end = datetime.datetime.now().microsecond

    print(f'insert sort: {end - start} ms')

    ints = [random.randint(0, 100) for _ in range(100)]

    start = datetime.datetime.now().microsecond
    print(fractal_sort(ints))
    end = datetime.datetime.now().microsecond

    print(f'fractal sort: {end - start} ms')
