import sqlite3
from os.path import exists

db_adress = "./db/todos.sqlite"


def connect_sqli():
    conn = sqlite3.connect(db_adress)
    return conn


def init_table():
    conn = connect_sqli()
    cur = conn.cursor()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    completed INTEGER)''')
    conn.commit()
    cur.close()
    conn.close()


def create(task_name: str):
    conn = connect_sqli()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO todos (name, completed) VALUES (?, 0)", (task_name,))
    conn.commit()
    cur.close()
    conn.close()

# READS ALL TODOS


def read_all():
    if not exists(db_adress):
        init_table()
    conn = connect_sqli()
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


# Function to read a single task from the todos table by ID
def read_one(id: int):
    conn = connect_sqli()
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos WHERE id=?", (id,))
    task = cur.fetchone()
    cur.close()
    conn.close()
    return task


# Function to update a task in the todos table
def update(task_id: int, new_name: str, completed: bool):
    conn = connect_sqli()
    cur = conn.cursor()
    cur.execute("UPDATE todos SET name=?, completed=? WHERE id=?",
                (new_name, completed, task_id))
    conn.commit()
    cur.close()
    conn.close()


# Function to mark a task as completed in the todos table
def complete(task_id: int):
    conn = connect_sqli()
    cur = conn.cursor()
    cur.execute("UPDATE todos SET completed=1 WHERE id=?", (task_id,))
    conn.commit()
    cur.close()
    conn.close()


# Function to delete a task from the todos table
def delete(task_id: int):
    conn = connect_sqli()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id=?", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
