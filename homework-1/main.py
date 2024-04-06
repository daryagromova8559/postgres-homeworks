"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

try:
    conn_parms = {
        "host": "localhost",
        "database": "north",
        "user": "postgres",
        "password": "02051996"
    }
    with psycopg2.connect(**conn_parms) as conn:
        with conn.cursor() as cur:
            with open(f"north_data/employees_data.csv") as employees_file:
                header = next(employees_file)
                reader = csv.reader(employees_file)
                for row in reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
            with open(f"north_data/customers_data.csv") as customers_file:
                header = next(customers_file)
                reader = csv.reader(customers_file)
                for row in reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
            with open(f"north_data/orders_data.csv") as orders_file:
                header = next(orders_file)
                reader = csv.reader(orders_file)
                for row in reader:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)
finally:
    conn.close()
