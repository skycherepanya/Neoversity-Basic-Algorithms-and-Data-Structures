import heapq
"""
Щоб витратити найменше сил на з'єднання кабелів, треба завжди брати два найкоротші шматки, з'єднувати їх, і класти новий шматок назад у купу.
"""

def min_cost(cables):
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        # 1. Дістаємо два найкоротші шматки
        first_shortest = heapq.heappop(cables)
        second_shortest = heapq.heappop(cables)
        
        # 2. З'єднуємо їх
        current_connection = first_shortest + second_shortest
        
        # 3. Додаємо це з'єднання до загальних витрат
        total_cost += current_connection
        
        # 4. Кладемо новий кабель назад у купу
        heapq.heappush(cables, current_connection)
        
    return total_cost

if __name__ == "__main__":
    network_cables = [4, 10, 3, 5, 1]
    
    print(f"Кабелі: {network_cables}")
    result = min_cost(network_cables)
    print(f"Мінімальні витрати на з'єднання: {result}")