import asyncio



async def slow_operation():
    await asyncio.sleep(2)
    return "Operation complete"

async def main():
    future = asyncio.ensure_future(slow_operation())
    # Do other things if needed
    result = await future
    print(result)

# Run the event loop
asyncio.run(main())
