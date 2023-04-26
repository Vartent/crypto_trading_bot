import asyncio
from models import Iterations
from crypto_http import get_btc_dominance, get_btc_price_change, get_eth_price_change


async def process_basic_price(storage: Iterations):
    """
    :param storage:
    prop to store info about price changing

    :return: basic price change

    alert when the price change went over 1%

    """

    btc_price_change, \
    eth_price_change, \
    btc_dominance = await asyncio.gather(
        get_btc_price_change(),
        get_eth_price_change(),
        get_btc_dominance())

    if btc_price_change and eth_price_change and btc_dominance:
        eth_basic_change = eth_price_change - (btc_price_change * btc_dominance / 100)
        storage.add_iteration(eth_basic_change)
        print(f"BTC Price difference: {round(btc_price_change, 4)} %,\n"
              f"ETH Price difference: {round(eth_price_change, 4)} %,\n"
              f"BTC Dominance: {round(btc_dominance, 4)}\n"
              f"Basic ETH difference {round(eth_basic_change, 4)} %\n"
              f"Current largest difference: {round(storage.current_largest_difference, 4)} %\n")

        # alert when the change is larger than 1%.
        # To be changed to telegram bot notification
        if storage.current_largest_difference >= 1:
            print(f"-------------------------------------\n"
                  f"BASIC PRICE CHANGE: {round(storage.current_largest_difference, 2)}\n"
                  f"-------------------------------------")

        return eth_basic_change
    else:
        print("Error getting data")
