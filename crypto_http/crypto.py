import asyncio
import aiohttp
import ssl

async def fetch_data(url, headers):
    """
    :param url: api url
    :param headers: fetch headers
    :return: api request result

    creating ClientSession within with block to increase performance
    """
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl_context=ssl_context)
    ) as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(response.status)


async def get_btc_price_change():
    """
    fetch BTC/USDT pair candle to calculate its percentage change

    :return: price change percent
    """
    url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=2"
    data = await fetch_data(url, headers=None)
    if data:
        open_price = float(data[0][1])
        close_price = float(data[0][4])
        price_change_percent = ((close_price - open_price) / open_price) * 100
        return price_change_percent
    else:
        return None


async def get_eth_price_change():
    """
    fetch ETH/USDT pair candle to calculate its percentage change
    :return: price change percent
    """
    url = "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=2"
    data = await fetch_data(url, headers=None)
    if data:
        open_price = float(data[0][1])
        close_price = float(data[0][4])
        price_change_percent = ((close_price - open_price) / open_price) * 100
        return price_change_percent
    else:
        return None


async def get_btc_dominance():
    """
    fetch BTC dominance

    api documentation: https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesLatest

    :return:
    """
    url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?convert=USD"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "8c7553f6-4f3f-4d82-88c8-4118ac9ac2d4"
    }
    data = await fetch_data(url, headers=headers)
    if data:
        return data["data"]["btc_dominance"]
    else:
        return None