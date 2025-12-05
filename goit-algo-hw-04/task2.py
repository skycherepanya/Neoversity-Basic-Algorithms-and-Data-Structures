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


def merge_k_lists(lists):
    result = lists[0]
    
    for i in range(1, len(lists)):
        result = merge(result, lists[i])
        
    return result


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    final_list = merge_k_lists(lists)
    print("Результат:", final_list)