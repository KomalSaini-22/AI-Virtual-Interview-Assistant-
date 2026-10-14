# import sqlite3

# conn = sqlite3.connect("database/interview.db")

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS interview(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# question TEXT,
# answer TEXT,
# score INTEGER
# )
# """)

# conn.commit()


import sqlite3

conn = sqlite3.connect("database/interview.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interviews(

id INTEGER PRIMARY KEY AUTOINCREMENT,

question TEXT,

answer TEXT,

score INTEGER

)
""")

conn.commit()


def save_answer(question, answer, score):

    cursor.execute(

        "INSERT INTO interviews(question,answer,score) VALUES(?,?,?)",

        (question, answer, score)

    )

    conn.commit()


def get_all_data():

    cursor.execute("SELECT * FROM interviews")

    return cursor.fetchall()