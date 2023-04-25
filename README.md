# crypto_trading_bot

## this is a task solution for job application

### the task is to find so called Basic Price of the **ETH/USDT** pair   
### since the **BTC** affects other litecoins, we need to neutralize its influence

First we get the **ETH/USDT** and **BTC/USDT** 1m derivative and convert it to percent.   
Then multuply the **BTC/USDT** percent change by BTC's dominance.   
Next we subtract **BTC/USDT** with indluence correction from **ETH/USDT** percent difference.   

Log in colsole when the *BASIC PRICE* of **ETH/USDT** changes by more than 1%

Fetching data from both https://binance.com/ and https://coinmarketcap.com/

*soon to add telegram bot for more flexible functionality*
