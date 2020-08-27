import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='banco_sabado',
                                         user='root',
                                         password='')
    if connection.is_connected():
        #db_Info = connection.get_server_info()
        #print("Conectado MySql e informa sua versão ", db_Info)
        # Cria um cursor:
        cursor = connection.cursor()

        # Executa o comando:
        cursor.execute("INSERT INTO clientes_fazenda (nome, email, telefone) VALUES ('Susie', 'susie@teste', 12345)")

        # Efetua um commit no banco de dados.
        # Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
        # suas alterações.
        connection.commit()

        # Executa o comando:
        cursor.execute("SELECT * FROM clientes_fazenda  ")

        # Busaca o resultado no banco:
        resultado = cursor.fetchall()

        # Mostra o resultado:
        print('Nome do cliente: ')

        for linha in resultado :
            print(linha)

except Error as e:
    print("Erro ao conectar MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL conexão fechada!")