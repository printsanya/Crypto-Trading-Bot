from dotenv import load_dotenv
import os
from bot import BasicBot  # import your class from bot.py

def main():
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    bot = BasicBot(api_key, api_secret)

    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    order_type = input("Enter order type (MARKET or LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))

    if order_type == "MARKET":
        order = bot.place_market_order(symbol, side, quantity)
    elif order_type == "LIMIT":
        price = float(input("Enter limit price: "))
        order = bot.place_limit_order(symbol, side, quantity, price)
    else:
        print("Invalid order type.")
        return

    if order:
        print("Order placed successfully!")
        print(order)
    else:
        print("Order failed. Check logs for details.")

if __name__ == "__main__":
    main()
