import asyncio
from asyncio import Task
from typing import Any
from utils import async_timed, delay


@async_timed()
async def cpu_bound_work() -> int:
    counter: int = 0
    for i in range(100_000_000):
        counter += 1
    return counter


@async_timed()
async def main() -> None:
    task_one: Task[Any] = asyncio.create_task(cpu_bound_work())
    task_two: Task[Any] = asyncio.create_task(cpu_bound_work())
    task_delay: Task[int] = asyncio.create_task(delay(4))
    await task_one
    await task_two
    await task_delay


asyncio.run(main())
