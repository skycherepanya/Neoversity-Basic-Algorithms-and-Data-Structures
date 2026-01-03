# Наше меню: назва -> ціна і калорії
menu = {
    "pizza": {"price": 50, "calories": 300},
    "hamburger": {"price": 40, "calories": 250},
    "hot-dog": {"price": 30, "calories": 200},
    "pepsi": {"price": 10, "calories": 100},
    "cola": {"price": 15, "calories": 220},
    "potato": {"price": 25, "calories": 350}
}

def greedy_algorithm(items, money_limit):
    # Створюємо список, щоб зручно сортувати
    food_list = []
    
    for name, info in items.items():
        price = info["price"]
        cal = info["calories"]
        # Рахуємо, скільки калорій ми отримуємо за 1 монету
        efficiency = cal / price 
        food_list.append((name, price, cal, efficiency))
    
    # Сортуємо: спочатку найвигідніші (де більше калорій за менші гроші)
    food_list.sort(key=lambda x: x[3], reverse=True)
    
    chosen_food = []
    total_cal = 0
    current_money = money_limit
    
    for food in food_list:
        name = food[0]
        price = food[1]
        cal = food[2]
        
        # Якщо вистачає грошей - беремо
        if price <= current_money:
            chosen_food.append(name)
            current_money -= price
            total_cal += cal
            
    return chosen_food, total_cal

def dynamic_programming(items, money_limit):
    # Перетворюємо словник у список, щоб звертатися за індексами
    names = list(items.keys())
    prices = [items[n]["price"] for n in names]
    calories = [items[n]["calories"] for n in names]
    
    count = len(items)
    
    # Створюємо таблицю для розрахунків
    table = [[0 for _ in range(money_limit + 1)] for _ in range(count + 1)]
    
    for i in range(1, count + 1):
        for w in range(money_limit + 1):
            price = prices[i-1]
            cal = calories[i-1]
            
            if price <= w:
                table[i][w] = max(table[i-1][w], cal + table[i-1][w-price])
            else:
                table[i][w] = table[i-1][w]
                
    # Тепер треба відновити список страв
    selected_items = []
    w = money_limit
    
    for i in range(count, 0, -1):
        if table[i][w] != table[i-1][w]:
            selected_items.append(names[i-1])
            w -= prices[i-1]
            
    return selected_items, table[count][money_limit]

if __name__ == "__main__":
    my_budget = 100
    
    print(f"Мій бюджет: {my_budget}")
    
    # Запуск жадібного
    g_items, g_cal = greedy_algorithm(menu, my_budget)
    print(f"Жадібний вибір: {g_items}, Калорії: {g_cal}")
    
    # Запуск динамічного
    d_items, d_cal = dynamic_programming(menu, my_budget)
    print(f"Динамічний вибір: {d_items}, Калорії: {d_cal}")