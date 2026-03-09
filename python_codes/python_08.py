import asyncio
import time
async def test():
    print('test')
    await asyncio.sleep(2)
    #time.sleep(2) # This will block the entire event loop, so it should be avoided in async code
    print('test completed')


async def main():
    start = time.time()
    await asyncio.gather(test(), test(), test())
    end = time.time()
    print(f'Total time taken: {end - start} seconds')

if __name__ == '__main__':
    asyncio.run(main())