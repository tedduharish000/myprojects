
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# MySQL connection details
USER = "root"
PASSWORD = "Harish@143"
HOST = "localhost"
DATABASE = "weather_data"

# Create an engine instance
engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}")

# Function to create a sample DataFrame
def create_sample_dataframe():
    data = {
        'city': ['London'],
        'temperature': [22.5],
        'humidity': [60],
        'weather_description': ['Clear sky'],
        'wind_speed': [5.0],
        'timestamp': [datetime.now()]
    }
    return pd.DataFrame(data)

# Insert data into MySQL
def save_to_mysql(data_frame):
    data_frame.to_sql('weather', con=engine, if_exists='append', index=False)
    print("Data saved to MySQL database.")

# Create a sample DataFrame
df = create_sample_dataframe()
print("DataFrame created:")
print(df)

# Save DataFrame to MySQL
save_to_mysql(df)
