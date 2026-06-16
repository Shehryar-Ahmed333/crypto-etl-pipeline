


# =====================================================================================================================================

import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

# ==========================================
# 1. EXTRACT (Fetch live data from the internet)
# ==========================================
def extract_data():
    print("🔄 1. Extracting live crypto data from API...")
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,  # Fetch top 10 coins
        'page': 1
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error: Status Code {response.status_code}")

# ==========================================
# 2. TRANSFORM (Clean and structure data using Pandas)
# ==========================================
def transform_data(raw_data):
    print("🧹 2. Transforming and cleaning data using Pandas...")
    df = pd.DataFrame(raw_data)
    
    # Select only the required columns
    columns_to_keep = ['id', 'name', 'symbol', 'current_price', 'market_cap', 'total_volume']
    df = df[columns_to_keep]
    
    # Data Cleaning: Handle missing values by replacing Nulls with 0
    df.fillna({'current_price': 0, 'market_cap': 0, 'total_volume': 0}, inplace=True)
    
    # Data Engineering Standard: Add an audit timestamp column
    df['extracted_at'] = datetime.now()
    
    return df

# ==========================================
# 3. LOAD (Insert data into PostgreSQL using SQLAlchemy)
# ==========================================
def load_data(df):
    print("🚀 3. Loading data into PostgreSQL via SQLAlchemy...")
    
    # Database Connection String
    conn_string = "postgresql://postgres:Your_Password@localhost:5432/postgres"
    
    # Create SQLAlchemy Engine
    engine = create_engine(conn_string)
    
    # Automatically create the table and insert the Pandas DataFrame into PostgreSQL
    df.to_sql('live_cryptos', con=engine, if_exists='replace', index=False)
    print("🎉 ETL Pipeline executed successfully! Data saved to 'live_cryptos' table.")

# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    try:
        data = extract_data()
        cleaned_df = transform_data(data)
        load_data(cleaned_df)
    except Exception as e:
        print(f"❌ Pipeline failed! Reason: {e}")