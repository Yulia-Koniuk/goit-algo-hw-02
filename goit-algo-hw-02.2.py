from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли та перетворюємо у нижній регістр
    s = s.replace(" ", "").lower()
    
    # Створюємо двосторонню чергу (deque)
    char_queue = deque()
    
    # Додаємо символи рядка до черги
    for char in s:
        char_queue.append(char)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True

# Приклад використання:
mixed_list = [
    "A man a plan a canal Panama",
    "Hello, world!",
    "Aibohphobia",
    "You are awesome",
    "Natasha, Natasha, ty moye sertse i dusha",
    "Madam, in Eden, I'm Adam",
    "Python programming language",
    "Was it a car or a cat I saw?",
    "O, Anna, Anna, O",
    "Slava Ukrayini",
    "Racecar",
    "This is not a palindrome",
    "Step on no pets",
    "Mr. Owl ate my metal worm",
    "Palindrome"
]

print("Перевірка змішаного списку:")
for word in mixed_list:
    print(f"{word}: {is_palindrome(word)}")

