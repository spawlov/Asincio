import asyncio
from utils import async_timed


@async_timed()
async def delay(delay_second: int) -> int:
    print(f"засыпаю на {delay_second}сек.")
    await asyncio.sleep(delay_second)
    print(f"сон в течении {delay_second}сек. закончился")
    return delay_second


@async_timed()
async def main() -> None:
    task_one: asyncio.Task[int] = asyncio.create_task(delay(2))
    task_two: asyncio.Task[int] = asyncio.create_task(delay(3))

    await task_one
    await task_two


asyncio.run(main())
