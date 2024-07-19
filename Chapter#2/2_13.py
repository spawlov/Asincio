import asyncio
from utils import delay


async def main() -> None:
    task: asyncio.Task[int] = asyncio.create_task(delay(10))

    try:
        result: int = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Задача заняла более 5сек. скоро она закончится!")
        result = await task
        print(result)


asyncio.run(main())
