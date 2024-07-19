import asyncio
from asyncio import Future


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future: Future) -> None:
    await asyncio.sleep(1)
    future.set_result(42)


async def main() -> None:
    future: Future = make_request()
    print(f"Будущий объект готов? {future.done()}")
    value: Future = await future
    print(f"Будущий объект готов? {future.done()}")
    print(value)


asyncio.run(main())
