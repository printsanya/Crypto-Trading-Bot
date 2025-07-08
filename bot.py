from binance.client import Client
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        
        logging.basicConfig(filename='bot.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )
            logging.info(f"Market Order: {order}")
            return order
        except Exception as e:
            logging.error(f"Market Order Error: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='LIMIT',
                price=price,
                quantity=quantity,
                timeInForce='GTC'
            )
            logging.info(f"Limit Order: {order}")
            return order
        except Exception as e:
            logging.error(f"Limit Order Error: {e}")
            return None
