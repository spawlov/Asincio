import functools
import time
from typing import Callable, Any


def async_timed() -> Callable[..., Callable[..., Any]]:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"выполняется {func} с аргументами {args} {kwargs}")
            start: float = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end: float = time.time()
                total: float = end - start
                print(f"{func} завершилась за {total:.4f}")

        return wrapped

    return wrapper
