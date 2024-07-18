import asyncio


async def delay(delay_second: int) -> int:
    print(f"засыпаю на {delay_second}сек.")
    await asyncio.sleep(delay_second)
    print(f"сон в течении {delay_second}сек. закончился")
    return delay_second
