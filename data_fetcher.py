import requests

def get_live_price(coin_id="bitcoin"):
    """Fetches raw data from CoinGecko API with error handling."""
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {'ids': coin_id, 'vs_currencies': 'usd', 'include_24hr_change': 'true'}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() 
        return response.json()
    except Exception as e:
        print(f"API Error: {e}")
        return None
