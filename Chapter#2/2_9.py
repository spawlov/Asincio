import asyncio

from utils import delay


async def main() -> None:
    sleep_for_three: asyncio.Task[int] = asyncio.create_task(delay(3))
    sleep_again: asyncio.Task[int] = asyncio.create_task(delay(3))
    sleep_once_more: asyncio.Task[int] = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_once_more


asyncio.run(main())
