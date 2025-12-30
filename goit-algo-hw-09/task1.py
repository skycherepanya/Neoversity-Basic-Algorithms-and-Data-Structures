import time

def find_coins_greedy(amount):
    """
    Жадібний алгоритм: йдемо від найбільшого номіналу до найменшого.
    Швидкість: O(N).
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount = amount % coin
            
    return result

def find_min_coins(amount):
    """
    Динамічне програмування: будуємо таблицю мінімальної кількості монет 
    для кожної суми від 0 до amount.
    Швидкість: O(A * N). Дуже повільно для великих сум.
    """
    coins = [50, 25, 10, 5, 2, 1]
    
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    
    used_coins = [0] * (amount + 1)
    
    for s in range(1, amount + 1):
        for coin in coins:
            if s >= coin:
                if min_coins[s - coin] + 1 < min_coins[s]:
                    min_coins[s] = min_coins[s - coin] + 1
                    used_coins[s] = coin
    
    result = {}
    current_sum = amount
    while current_sum > 0:
        coin = used_coins[current_sum]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_sum -= coin
        
    return result

if __name__ == "__main__":
    sum_test = 113
    print(f"Сума: {sum_test}")
    print(f"Жадібний: {find_coins_greedy(sum_test)}")
    print(f"Динамічний: {find_min_coins(sum_test)}")
    
    large_sum = 10000
    
    start_time = time.time()
    find_coins_greedy(large_sum)
    greedy_time = time.time() - start_time
    
    start_time = time.time()
    find_min_coins(large_sum)
    dp_time = time.time() - start_time
    
    print(f"Час для суми {large_sum}:")
    print(f"Greedy: {greedy_time:.6f} сек")
    print(f"DP: {dp_time:.6f} сек")