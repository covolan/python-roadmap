import heapq

li = [5, 7, 9, 1, 3]

heapq.heapify(li)
print(li)

heapq.heappush(li, 5)
print(li)

heapq._heapify_max(li)
print(li)


