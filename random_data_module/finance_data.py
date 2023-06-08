"""
Use Alpha vantage API to get stock dat and plot it in a graph
"""
import requests
import pandas
import matplotlib.pyplot as plt



API_KEY="RTART83NP1RD7G8X"
symbol = "MSFT"

def get_daily_stock_data(symbol: str):
    """
    Use Alpha vantage API to get stock dat and plot it in a graph
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

def main():
    data = get_daily_stock_data(symbol)

    # Turn the data into a pandas DF
    df = pandas.DataFrame.from_dict(data["Time Series (Daily)"])
    df.index = pandas.to_datetime(df.index)
    df = df.sort_index(ascending=False)

    # Plot the data
    df.plot()
    
    
    pass


if __name__ == "__main__":
    main()