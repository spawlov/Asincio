import asyncio

from utils import delay


async def main() -> None:
    sleep_for_three: asyncio.Task[int] = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result: int = await sleep_for_three
    print(result)


asyncio.run(main())
