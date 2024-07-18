import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def main() -> None:
    one_plus_one: int = await add_one(1)
    two_plus_one: int = await add_one(2)
    print(one_plus_one)
    print(two_plus_one)


asyncio.run(main())
