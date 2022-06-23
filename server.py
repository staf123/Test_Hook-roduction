import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
           "SELECT version();"
       )
        print(f"Server version: {cursor.fetchone()}")
    cursor.execute(" INSERT OR IGNORE INTO 'users' ('user_id') VALUES (?)" (1000,))

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL, _ex")
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
