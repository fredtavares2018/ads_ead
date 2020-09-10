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

    #print("Nome:",cad1)
    # print("Email:",cad2)
    #print("Telefone",cad3)

    # se for usar mysql, trocar ? por %
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nome text, telefone integer)")
    comando_SQL = "INSERT INTO clientes VALUES (?,?)"
    dados = (str(cad1),str(cad3))
    cursor.execute(comando_SQL, dados)
    banco.commit()
    # aqui limpamos os campos do cadastro
    cadastros.lineEdit.setText("")
    cadastros.lineEdit_3.setText("")

    # cursor.execute("SELECT * FROM clientes")
    # print(cursor.fetchall())


def listar_clientes():
    listagem.show()

    cursor = banco.cursor()
    cursor.execute("SELECT * FROM clientes")
    receber_dados = cursor.fetchall()
    # print(receber_dados)

    listagem.tela_mostragem.setRowCount(len(receber_dados))
    listagem.tela_mostragem.setColumnCount(2)

    for i in range(0, len(receber_dados)):
        for j in range(0, 2):
            listagem.tela_mostragem.setItem(i,j,QtWidgets.QTableWidgetItem(str(receber_dados[i][j])))


app=QtWidgets.QApplication([])
cadastros=uic.loadUi("cadastro.ui")
listagem=uic.loadUi("listagem.ui")
cadastros.pushButton.clicked.connect(cadastro_clientes)
cadastros.but_listagem.clicked.connect(listar_clientes)

cadastros.show()
app.exec()
