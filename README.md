# Crypto ETL Pipeline

A production-ready Data Engineering ETL (Extract, Transform, Load) pipeline built with Python, Pandas, and PostgreSQL.

## Core Architecture
1. **Extract**: Fetches top 10 cryptocurrency markets data from CoinGecko REST API using `requests`.
2. **Transform**: Cleans incoming data, handles missing values, and adds an audit column (`extracted_at` timestamp) using `pandas`.
3. **Load**: Ingests the structured data into a local `PostgreSQL` database instance automatically via `SQLAlchemy`.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: Pandas, Requests, SQLAlchemy
- **Database**: PostgreSQL

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install pandas requests sqlalchemy psycopg2-binary`
3. Update your database password in `etl_pipeline.py`.
4. Run the pipeline: `python etl_pipeline.py`
