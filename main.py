from enum import unique
from database import db_utils as db
from extraction_scripts import namesExtractor
import os


# we use this sciprt to insert to the new table the unique names
# namesExtractor.insert_into_people()

config = {
        "URL": os.getenv("URL"),
        "PORT": os.getenv("PORT"),
        "User": os.getenv("USER"),
        "Password": os.getenv("PASSWORD"),
        "Name": os.getenv("DATABASE_NAME"),
    }

connection = db.get_connection(config)


