import pandas as pd
from datetime import datetime

def clean_data(raw_json, coin_id):
    """Converts raw JSON into a structured, timestamped DataFrame."""
    if not raw_json or coin_id not in raw_json:
        return None

    data = raw_json[coin_id]
    
    record = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'coin': coin_id.upper(),
        'price_usd': data['usd'],
        'change_24h': round(data['usd_24h_change'], 2)
    }
    
    return pd.DataFrame([record])
