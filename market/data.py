import sqlite3

from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
data = DB_FILE
TABLE_NAME = "products"


def create_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
        "("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "NAME VARCHAR(255) NOT NULL,"
        "VALUE REAL NOT NULL,"
        "AMOUNT INTEGER NOT NULL"
        ")"
    )
    connection.commit()
    cursor.close()
    connection.close()


def dellAllTable():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM {TABLE_NAME}")
    connection.commit()
    cursor.close()
    connection.close()


def addProduct(list):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    sql = f"INSERT INTO {TABLE_NAME}(NAME, VALUE, AMOUNT) " f"VALUES ( :name, :value, :amount )"

    cursor.execute(sql, (list))
    connection.commit()
    cursor.close()
    connection.close()


def selectAllProduct():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {TABLE_NAME}")

    for row in cursor.fetchall():
        _id = row[0]
        name = row[1]
        value = row[2]
        amount = row[3]
        print(_id, name, value, amount)

    cursor.close()
    connection.close()


def selectForId(numberId):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    sql = f"SELECT * FROM {TABLE_NAME} " f"WHERE id = ? "

    cursor.execute(sql, numberId)
    row = cursor.fetchone()
    print(row)

    cursor.close()
    connection.close()
