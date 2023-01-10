import array as arr


def sort_by_size(array_input):

    temp_array = arr.array('i')
    counter = 0

    for i in array_input:
        counter += 1

    for i in range(0, counter):
        temp_array.append(i)

    for i, j in enumerate(temp_array):
        if not j in array_input:
            temp_array.remove(j)
            temp_array.insert(i, -1)

    return temp_array


array_1 = arr.array('i', [19, 7, 0, 3, 18, 15, 12, 6,
                    1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4])

array_2 = sort_by_size(array_1)

print('\n')
for i in array_2:
    print(i, end=', ')
print('\n')
