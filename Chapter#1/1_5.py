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


start: float = time.time()

fibs_no_threding()

end: float = time.time()

print(f"Время работы {end - start:.4f}сек.")
