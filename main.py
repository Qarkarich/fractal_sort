import datetime
import random


def split_in_groups(data):
    item_groups = {}

    for item in data:
        if item in item_groups:
            item_groups[item].append(item)
        else:
            item_groups[item] = [item]

    res = []

    for group in sorted(item_groups.keys()):
        res.extend(item_groups[group])

    return res


def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


if __name__ == '__main__':
    ints = [random.randint(0, 10000) for _ in range(1000)]

    start = datetime.datetime.now().microsecond
    bubble_sort(ints)
    end = datetime.datetime.now().microsecond

    print(f'bubble sort: {end - start} ms')

    start = datetime.datetime.now().microsecond
    print(split_in_groups(ints))
    end = datetime.datetime.now().microsecond

    print(f'amazing sort: {end - start} ms')

    start = datetime.datetime.now().microsecond
    ints.sort()
    end = datetime.datetime.now().microsecond

    print(f'python default sort: {end - start} ms')
