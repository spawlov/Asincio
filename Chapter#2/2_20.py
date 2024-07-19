import asyncio
from typing import Any
import requests
from utils import async_timed


@async_timed()
async def get_pyhon_status() -> int:
    return requests.get("https://python.org").status_code


@async_timed()
async def main():
    task_1: asyncio.Task[Any] = asyncio.create_task(get_pyhon_status())
    task_2: asyncio.Task[Any] = asyncio.create_task(get_pyhon_status())
    task_3: asyncio.Task[Any] = asyncio.create_task(get_pyhon_status())
    await task_1
    await task_2
    await task_3


asyncio.run(main())
