import sqlite3

banco = sqlite3.connect('tb_clientes.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE usuarios (nome text, telefone integer)")

nome = 'teste 2'
telefone = 12345

cursor.execute("INSERT INTO usuarios VALUES(?,?)", (nome,telefone))

banco.commit()

cursor.execute("SELECT * FROM usuarios")

print(cursor.fetchall())