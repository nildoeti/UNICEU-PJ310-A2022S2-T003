import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO empresa (nome, telecom) VALUES (?, ?)",
            ('Univesp', '11 - 000000000')
            )

cur.execute("INSERT INTO empresa (nome, telecom) VALUES (?, ?)",
            ('Univesp2', '11 - 000000000')
            )



#posts 2


cur.execute("INSERT INTO escola (nome, grau, horario) VALUES (?, ?, ?)",
            ('Univesp', '2° grau', '12:00 - 13:00')
            )

cur.execute("INSERT INTO escola (nome, grau, horario) VALUES (?, ?, ?)",
            ('Univesp2', '2° grau', '12:00 - 13:00')
            )

connection.commit()
connection.close()