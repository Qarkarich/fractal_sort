def fractal_sort(data):
    keys = []
    for i in range(len(data)):
        for j in range(len(keys)):
            if data[i] in keys[j]:
                keys[j].append(data[i])
                break
        else:
            keys.append([data[i]])

    data = [num for item in sorted(keys) for num in item]

    return data
