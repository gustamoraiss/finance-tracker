import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    valor REAL NOT NULL,
    tipo TEXT NOT NULL,
    categoria TEXT NOT NULL,
    data DATE NOT NULL,
    descricao TEXT
    );''')
conn.commit()

conn.close()