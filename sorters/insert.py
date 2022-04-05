def insert_sort(data):
    for i in range(1, len(data)):
        j = i - 1
        while j >= 0 and data[i] < data[j]:
            data[j + 1] = data[i]
            j -= 1
        data[j + 1] = data[i]

    return data
