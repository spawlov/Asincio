import asyncio

from utils import delay


async def hello_every_second() -> None:
    for i in range(2):
        await asyncio.sleep(1)
        print("пока я жду, исполняется другой код")


async def main() -> None:
    first_delay: asyncio.Task[int] = asyncio.create_task(delay(3))
    second_delay: asyncio.Task[int] = asyncio.create_task(delay(3))

    await hello_every_second()
    await first_delay
    await second_delay


asyncio.run(main())
