import threading
import time

def write_words(word_cout: int, file_name: str):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(1, word_cout + 1):
            time.sleep(0.1)
            file.write(f'Какое-то слово № {i}\n')
    print(f'Завершилась запись файла {file_name}')
start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_time = time.time()
print(f'Работа функций, {time.strftime('%0:%M:%S', time.localtime(finish_time - start_time))}')
start_time = time.time()
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
finish_time = time.time()
print(f'Работа потоков, {time.strftime('%0:%M:%S', time.localtime(finish_time - start_time))}')