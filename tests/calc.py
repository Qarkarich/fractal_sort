from random import randint
from timeit import default_timer as timer

from numpy import mean


def generate_data(size):
    return [randint(0, 100) for _ in range(size)]


def calculate_average_performance(iterations, alg, default_list=None, data_size=None):
    performance_data = []

    if default_list:
        for _ in range(iterations):
            start = timer()
            alg(default_list)
            end = timer()
            elapsed_time = end - start
            performance_data.append(elapsed_time)
    else:
        integers_list = generate_data(data_size)
        for _ in range(iterations):
            start = timer()
            alg(integers_list)
            end = timer()
            elapsed_time = end - start
            performance_data.append(elapsed_time)

    return mean(performance_data)
