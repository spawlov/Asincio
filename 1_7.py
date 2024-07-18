import threading
import time
import requests
from requests import Response


def read_example(url: str) -> None:
    response: Response = requests.get(url)
    print(response.status_code)


sync_start: float = time.time()
read_example("https://python.org")
read_example("https://python.org")
sync_end: float = time.time()
print(f"Синхронное выполнение заняло {sync_end - sync_start:.4f}сек.")

thread_1 = threading.Thread(target=read_example, args=("https://python.org",))
thread_2 = threading.Thread(target=read_example, args=("https://python.org",))

thread_start: float = time.time()
thread_1.start()
thread_2.start()
print("Все потоки работают!")
thread_1.join()
thread_2.join()
thread_end: float = time.time()
print(f"Многопоточное выполнение заняло {thread_end - thread_start:.4f}сек.")
