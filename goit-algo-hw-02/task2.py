from collections import deque

def is_palindrome(text):
    # 1. Підготовка тексту
    processed_text = text.lower().replace(" ", "")
    # 2. Створюємо двосторонню чергу і додаємо туди символи
    char_deque = deque(processed_text)

    while len(char_deque) > 1:
        first_char = char_deque.popleft()
        last_char = char_deque.pop()
     # 3. Порівнюємо символи з обох кінців
        if first_char != last_char:
            return False
        
    return True

print(is_palindrome("Привіт"))
print(is_palindrome("Дід"))