import os
from dotenv import load_dotenv, find_dotenv
import mysql.connector


# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

# Insert cleaned data to database
conn = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USERNAME"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_DATABASE"),
    port=os.environ.get("DB_PORT")
)

db = conn.cursor()
print(db)
