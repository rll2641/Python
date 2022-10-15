def insertion_sort(lst):
    for end in range(1, len(lst)): # 1, 2, 3, 4
        for i in range(end, 0, -1):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
    return lst

lst = [5, 1, 4, 2, 3]

print(insertion_sort(lst))