import asyncio
import time

async def fetch_data():
    print("Hi")
    await asyncio.sleep(3)
    print("Bye")

async def main():
    start_time = time.perf_counter()    # Start the timer

    # Create a list of tasks
    tasks = [fetch_data() for _ in range(2)]

    # Run tasks concurrently
    await asyncio.gather(*tasks)

    end_time = time.perf_counter()      # End the timer
    print(f"TOtal time taken: {end_time - start_time:.2f} seconds")

asyncio.run(main())