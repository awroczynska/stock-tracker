import requests

API_KEY = "demo"
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_price(symbol):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if "Global Quote" in data and data["Global Quote"]:
        quote = data["Global Quote"]
        print(f"\n📈 {symbol.upper()}")
        print(f"   Price:  ${quote['05. price']}")
        print(f"   Change: {quote['09. change']} ({quote['10. change percent']})")
        print(f"   High:   ${quote['03. high']}")
        print(f"   Low:    ${quote['04. low']}")
        print(f"   Volume: {quote['06. volume']}")
    else:
        print("Could not find stock. Try a different symbol.")

def main():
    print("=== STOCK PRICE TRACKER ===")
    print("Using Alpha Vantage API")
    print("Type 'quit' to exit\n")
    
    while True:
        symbol = input("Enter stock symbol (e.g. AAPL, TSLA, MSFT): ").strip()
        if symbol.lower() == "quit":
            print("Goodbye!")
            break
        if symbol:
            get_stock_price(symbol)

if __name__ == "__main__":
    main()