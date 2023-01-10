import sys
import array as arr

def find_3_largests(array):

    large_1 = large_2 = large_3 = - sys.maxsize

    for i in array:
        if i > large_1:
            large_3 = large_2
            large_2 = large_1
            large_1 = i
        elif i > large_2 and i != large_1:
            large_3 = large_2
            large_2 = i
        elif i > large_3 and i != large_2:
            large_3 = i

    print(large_1, large_2, large_3)

array_1 = arr.array('i', [10, 4, 3, 50, 23, 90])
find_3_largests(array_1)