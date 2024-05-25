
import sys
import os
from dotenv import load_dotenv
import psycopg2
# Connection parameters for the newly created database
load_dotenv()
user = os.environ['PG_USER']
password = os.environ['PG_PASSWORD']
host = os.environ['PG_HOST']
port = os.environ['PG_PORT']
database = os.environ['PG_DATABASE']

# Connect to the newly created database
conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port
)

cursor = conn.cursor()

# SQL commands to create tables
create_google_play_downloads_table = """
CREATE TABLE google_play_downloads (
    id SERIAL PRIMARY KEY,
    app_id TEXT NOT NULL,
    title TEXT NOT NULL,
    date DATE NOT NULL,
    installs INTEGER,
    ratings_count INTEGER,
    average_rating FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL
);
"""

create_telegram_channel_growth_table = """
CREATE TABLE telegram_channel_growth (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    channel_url TEXT NOT NULL,
    subscriber_count INTEGER
);
"""
create_google_play_reviews_table="""
CREATE TABLE google_play_reviews (
    id SERIAL PRIMARY KEY,
    review_id TEXT NOT NULL,
    user_name TEXT,
    user_image TEXT NOT NULL,
    at DATE NOT NULL,
    app_version INTEGER,
    score INTEGER NOT NULL
);

"""
create_telegram_post_performance_table="""
CREATE TABLE telegram_post_performance (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    post_link TEXT,
    views INTEGER,
    post_hour TIME,
    bank TEXT,
    time_of_day TEXT
);

"""
# Execute the SQL commands
try:
    cursor.execute(create_google_play_reviews_table)
    cursor.execute(create_telegram_post_performance_table)
    cursor.execute(create_google_play_downloads_table)
    cursor.execute(create_telegram_channel_growth_table)
    conn.commit()
    print("Tables created successfully.")
except Exception as e:
    print(f"Error creating tables: {e}")

# Close the cursor and connection
cursor.close()
conn.close()
