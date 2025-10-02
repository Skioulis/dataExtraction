from dotenv import load_dotenv
import os
import psycopg2
import db_utils as db

load_dotenv(dotenv_path="ENV files/.env")

config = {
    "URL": os.getenv("URL"),
    "PORT": os.getenv("PORT"),
    "User": os.getenv("USER"),
    "Password": os.getenv("PASSWORD"),
    "Name": os.getenv("DATABASE_NAME"),
}
composer_set = set()

try:
    connection = db.create_db_connection(config)
    print("Connection successful!")

    cursor = connection.cursor()
    query = "SELECT composer, writer FROM old_songs; "
    cursor.execute(query)
    composers = cursor.fetchall()
    # print(type(composers))

    for composer in composers:
        composer_set.add(composer[0])
        composer_set.add(composer[1])

except Exception as e:
    print("Error connecting to the database:", e)
finally:
    if 'connection' in locals() and connection:
        connection.close()

print(len(composer_set))

try:
    connection = db.create_db_connection(config)
    print("Connection successful!")

    cursor = connection.cursor()
    insert_query = """
            INSERT INTO people (name) 
            VALUES (%s)
            
                """

    for name in composer_set:
            cursor.execute(insert_query, (name,))
            print(f"Inserted {name} into people table.")

    connection.commit()
    print(f"Inserted {cursor.rowcount} new people.")

except Exception as e:
    print("Error inserting into people table:", e)
finally:
    if 'connection' in locals() and connection:
        connection.close()
