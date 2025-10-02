import psycopg2

def create_db_connection(config):
    """
    Creates and returns a database connection using the given configuration.

    This function uses psycopg2 to establish a connection to a PostgreSQL database
    with the specified parameters provided in the configuration dictionary.

    Args:
        config (dict): A dictionary containing configuration details for the database
            connection. Expected keys are:
            - "URL" (str): The database host URL.
            - "PORT" (int): The database connection port.
            - "User" (str): The username for authentication.
            - "Password" (str): The password for authentication.
            - "Name" (str): The name of the database.

    Returns:
        psycopg2.connection: An active connection to the specified PostgreSQL database.
    """
    return psycopg2.connect( host=config["URL"],
        port=config["PORT"],
        user=config["User"],
        password=config["Password"],
        dbname=config["Name"])