# utils/sql_runner.py

from db.mysql_handler import mysql_connection
from decimal import Decimal
import datetime

def serialize_value(v):
    """Convert MySQL non-JSON-serializable types to Python native types."""
    if isinstance(v, Decimal):
        return float(v)
    if isinstance(v, (datetime.date, datetime.datetime)):
        return str(v)
    return v

def serialize_rows(rows):
    """Apply serialize_value to every cell in every row."""
    return [[serialize_value(cell) for cell in row] for row in rows]

def run_custom_sql(sql: str):
    try:
        cursor = mysql_connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        headers = [col[0] for col in cursor.description]
        cursor.close()
        return headers, serialize_rows(rows)
    except Exception as e:
        return ["Error"], [[str(e)]]

def get_cursor():
    """
    Return a reusable MySQL cursor for custom use.
    Caller is responsible for closing the cursor.
    """
    return mysql_connection.cursor()
