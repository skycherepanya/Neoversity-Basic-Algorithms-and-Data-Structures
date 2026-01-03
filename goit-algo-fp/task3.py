import heapq

def dijkstra(graph, start_node):
    # Черга пріоритетів
    priority_queue = [(0, start_node)]
    
    shortest_times = {station: float('inf') for station in graph}
    shortest_times[start_node] = 0
    
    while priority_queue:
        current_time, current_station = heapq.heappop(priority_queue)

        # Якщо ми знайшли шлях довший, ніж вже відомий - пропускаємо
        if current_time > shortest_times[current_station]:
            continue

        # Перевіряємо сусідні станції
        for neighbor, travel_time in graph[current_station].items():
            time = current_time + travel_time
            
            # Якщо знайшли швидший шлях
            if time < shortest_times[neighbor]:
                shortest_times[neighbor] = time
                heapq.heappush(priority_queue, (time, neighbor))

    return shortest_times

# лінії метро Будапешту
m1 = [("Vörösmarty tér", "Deák Ferenc tér", 2), ("Deák Ferenc tér", "Oktogon", 3), ("Oktogon", "Hősök tere", 4)]
m2 = [("Széll Kálmán tér", "Batthyány tér", 2), ("Batthyány tér", "Deák Ferenc tér", 3), ("Deák Ferenc tér", "Astoria", 2), ("Astoria", "Keleti pályaudvar", 3)]
m3 = [("Nyugati pályaudvar", "Deák Ferenc tér", 3), ("Deák Ferenc tér", "Kálvin tér", 2), ("Kálvin tér", "Corvin-negyed", 2)]
m4 = [("Szent Gellért tér", "Kálvin tér", 3), ("Kálvin tér", "Keleti pályaudvar", 4), ("Keleti pályaudvar", "II. János Pál pápa tér", 2)]

# Об'єднуємо всі лінії в один список
all_lines = m1 + m2 + m3 + m4

# Будуємо граф
budapest_metro = {}

for station1, station2, time in all_lines:
    # Додаємо станції в словник, якщо їх там ще немає
    if station1 not in budapest_metro:
        budapest_metro[station1] = {}
    if station2 not in budapest_metro:
        budapest_metro[station2] = {}
    
    # Додаємо зв'язок в обидві сторони
    budapest_metro[station1][station2] = time
    budapest_metro[station2][station1] = time

# --- Запуск алгоритму ---
if __name__ == "__main__":
    start_station = "Széll Kálmán tér"
    print(f"Прораховано найкоротший шлях від: {start_station}")
    
    times = dijkstra(budapest_metro, start_station)
    
    for station, minutes in sorted(times.items(), key=lambda item: item[1]):
        print(f"До {station}: {minutes} хвилин")