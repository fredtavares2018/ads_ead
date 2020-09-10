import sqlite3

banco = sqlite3.connect('tb_clientes.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nome text, telefone integer)")

# variaveis
# nome = 'Fred'
# telefone = '1234'

# metodo de entrada de dados
nome = input('Digite um nome: ')
telefone = input('Digite um telefone: ')

cursor.execute("INSERT INTO usuarios VALUES(?, ?)",(nome, telefone))

banco.commit()

cursor.execute("SELECT * FROM usuarios")

print(cursor.fetchall())