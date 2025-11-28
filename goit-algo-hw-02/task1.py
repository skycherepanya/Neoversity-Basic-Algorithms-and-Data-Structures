from queue import Queue

#Створити чергу заявок
queue = Queue()
request_counter = 0

def generate_request():
    #Створити нову заявку
    global request_counter
    request_counter += 1
    #Додати заявку до черги
    queue.put(request_counter)
    print(f"Заявку {request_counter} додано до черги")


def process_request():
    #Якщо черга не пуста:
    if not queue.empty():
        #Видалити заявку з черги
        req = queue.get()
        #Обробити заявку
        print(f"Заявку {req} оброблено")
    #Інакше:
    else:
        #Вивести повідомлення, що черга пуста
        print("Черга пуста")

# Головний цикл програми:
print("Програма працює. Натисніть Enter для кроку або введіть 'exit' для виходу.")

#Поки користувач не вийде з програми:
while True:
    user_input = input()
    if user_input == "exit":
        break
    
#Виконати generate_request() для створення нових заявок
generate_request()
#Виконати process_request() для обробки заявок
process_request()