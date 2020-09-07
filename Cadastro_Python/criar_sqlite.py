import sqlite3

banco = sqlite3.connect('bc_clientes.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE clientes (nome text, telefone integer)")

nome = 'teste 2'
telefone = 12345

cursor.execute("INSERT INTO clientes VALUES(?,?)", (nome,telefone))

banco.commit()

cursor.execute("SELECT * FROM clientes")

print(cursor.fetchall())