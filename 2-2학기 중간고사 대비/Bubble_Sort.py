def bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        # swapped = 최적화(swap이 일어나지 않을 시, break)
        swapped = False
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

lst = [5, 1, 4, 2, 3]

print(bubble_sort(lst))