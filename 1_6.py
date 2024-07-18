from re import S
import threading
import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f"fib({number}) = {fib(number)}")


def fibs_no_threding():
    print_fib(40)
    print_fib(41)


def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))

    fortieth_thread.start()
    forty_first_thread.start()

    fortieth_thread.join()
    forty_first_thread.join()


start: float = time.time()
fibs_no_threding()
end: float = time.time()
print(f"Время работы {end - start:.4f}сек.")

start = time.time()
fibs_with_threads()
end = time.time()
print(f"Многопоточное вычисление заняло {end - start:.4f}сек.")
