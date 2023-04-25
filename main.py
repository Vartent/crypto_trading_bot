import asyncio
from models import Iterations
from config import MONITOR_RANGE
from services import process_basic_price


async def main():
    eth_storage = Iterations(MONITOR_RANGE)
    while True:
        await process_basic_price(eth_storage)
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
