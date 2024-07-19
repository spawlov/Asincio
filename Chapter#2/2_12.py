import asyncio
from utils import delay


async def main() -> None:
    delay_task: asyncio.Task[int] = asyncio.create_task(delay(2))
    try:
        result: int = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Тайм-аут!")
        print(f"Задача была снята? {delay_task.cancelled()}")


asyncio.run(main())
