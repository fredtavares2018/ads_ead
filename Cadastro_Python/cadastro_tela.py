from PyQt5 import  uic,QtWidgets
# import mysql.connector

# banco = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="banco_sabado"
# )

import sqlite3

banco = sqlite3.connect('bc_clientes.db')


def cadastro_clientes():
    cad1 = cadastros.lineEdit.text()
    # cad2 = cadastros.lineEdit_2.text()
    cad3 = cadastros.lineEdit_3.text()

    print("Nome:",cad1)
    # print("Email:",cad2)
    print("Telefone",cad3)

    # se for usar mysql, trocar ? por %
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO clientes VALUES (?,?)"
    dados = (str(cad1),str(cad3))
    cursor.execute(comando_SQL, dados)
    banco.commit()
    # aqui limpamos os campos do cadastro
    cadastros.lineEdit.setText("")
    cadastros.lineEdit_3.setText("")

    cursor.execute("SELECT * FROM clientes")
    print(cursor.fetchall())
    

app=QtWidgets.QApplication([])
cadastros=uic.loadUi("Cadastro_Python/cadastros.ui")
cadastros.pushButton.clicked.connect(cadastro_clientes)

cadastros.show()
app.exec()