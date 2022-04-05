def fractal_sort(data):
    keys = {}
    for i in range(len(data)):
        if data[i] in keys:
            keys[data[i]].append(data[i])
        else:
            keys[data[i]] = [data[i]]

    data = [num for item in sorted(keys) for num in keys[item]]

    yield data
