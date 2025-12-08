def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    return iterations, upper_bound


if __name__ == "__main__":
    arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
    x = 3.5

    result = binary_search(arr, x)
    
    print(f"Масив: {arr}")
    print(f"Шукаємо число >= {x}")
    print(f"Кількість ітерацій: {result[0]}")
    print(f"Верхня межа: {result[1]}") 