import psycopg2

def create_db_connection(config):
    return psycopg2.connect( host=config["URL"],
        port=config["PORT"],
        user=config["User"],
        password=config["Password"],
        dbname=config["Name"])