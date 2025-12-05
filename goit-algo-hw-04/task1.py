import random
import timeit


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


if __name__ == "__main__":
    for size in [100, 1000, 5000]:
        print(f"Перевіряємо список на {size} елементів")
        
        # Генеруємо список випадкових чисел
        data = [random.randint(0, 5000) for _ in range(size)]

        # Заміряємо Insertion Sort
        time_1 = timeit.timeit(lambda: insertion_sort(data[:]), number=1)
        print(f"Insertion Sort: {time_1} секунд")

        # Заміряємо Merge Sort
        time_2 = timeit.timeit(lambda: merge_sort(data[:]), number=1)
        print(f"Merge Sort: {time_2} секунд")

        # Заміряємо Timsort
        time_3 = timeit.timeit(lambda: sorted(data[:]), number=1)
        print(f"Timsort: {time_3} секунд")

        print("-" * 40)