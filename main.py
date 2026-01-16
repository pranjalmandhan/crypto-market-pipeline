from data_fetcher import get_live_price
from data_processor import clean_data
import os

def run_pipeline():
    target_coin = "bitcoin"
    print(f"Running ETL for {target_coin}...")

    raw = get_live_price(target_coin)
    
    df = clean_data(raw, target_coin)
    
    if df is not None:
        path = 'data/market_history.csv'
        os.makedirs('data', exist_ok=True)
        
        df.to_csv(path, mode='a', index=False, header=not os.path.exists(path))
        print("Data archived successfully.")
        print(df)

if __name__ == "__main__":
    run_pipeline()
