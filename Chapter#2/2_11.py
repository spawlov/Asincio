import asyncio
from asyncio import CancelledError, Task

from utils import delay


async def main() -> None:
    long_task: Task[int] = asyncio.create_task(delay(10))

    second_elapsed: int = 0

    while not long_task.done():
        print("Задача не закончилась. Следующая проверка через секунду.")
        await asyncio.sleep(1)
        second_elapsed += 1

        if second_elapsed >= 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print("Наша задача была снята")


asyncio.run(main())
