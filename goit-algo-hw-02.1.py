import queue
import random
import time
import threading

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    while True:
        request_id = random.randint(1000, 9999)
        print(f"Генерація нової заявки з ID: {request_id}")
        request_queue.put(request_id)
        time.sleep(random.uniform(0.5, 2))  # Затримка для імітації часу між заявками

# Функція для обробки заявок
def process_request():
    while True:
        if not request_queue.empty():
            request_id = request_queue.get()
            print(f"Обробка заявки з ID: {request_id}")
            time.sleep(random.uniform(1, 3))  # Затримка для імітації часу обробки заявки
            request_queue.task_done()
        else:
            print("Черга пуста, очікування нових заявок...")
            time.sleep(1)

# Головний цикл програми
def main():
    # Створення потоків для генерації та обробки заявок
    generator_thread = threading.Thread(target=generate_request)
    processor_thread = threading.Thread(target=process_request)
    
    # Запуск потоків
    generator_thread.start()
    processor_thread.start()
    
    # Зупинка потоків перед завершенням програми (необов'язково)
    generator_thread.join()
    processor_thread.join()

if __name__ == "__main__":
    main()
