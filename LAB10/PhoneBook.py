import psycopg2
import csv
def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="12345678"
    )
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("table was created")
def insert_from_console():
    name = input("print name: ")
    phone = input("phone number: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Success")
def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row['name'], row['phone']))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Info {filename} was added")
def update_data(old_name, new_name=None, new_phone=None):
    conn = connect()
    cur = conn.cursor()
    if new_name:
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, old_name))
    conn.commit()
    cur.close()
    conn.close()
    print(f"{old_name} updated")
def find_by_name(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print(f"no data {name}")
    cur.close()
    conn.close()
def delete_by_name(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print(f"{name} deleted")
create_table()
def delete_by_phone(phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    cur.close()
    conn.close()
    print(f"{phone} deleted")
def delete():
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook;")
    conn.commit()
    cur.close()
    conn.close()
    print("deleted")
def ID_restart():
    conn = connect()
    cur = conn.cursor()
    cur.execute("ALTER SEQUENCE phonebook_id_seq RESTART WITH 1;")
    conn.commit()
    cur.close()
    conn.close()
    print("ID restarted")
def view_all_data():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook;")
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    cur.close()
    conn.close()
#insert_from_console()
insert_from_csv('1.csv')
#update_data('a', new_name='John Smith', new_phone='1234567890')
#find_by_name('John')
#delete_by_name('a')
#delete_by_phone('1234560987')
#delete()
#ID_restart()
view_all_data()