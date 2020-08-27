from PyQt5 import  uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco_sabado"
)

def cadastro_clientes():
    cad1 = cadastros.lineEdit.text()
    cad2 = cadastros.lineEdit_2.text()
    cad3 = cadastros.lineEdit_3.text()

    print("Nome:",cad1)
    print("Email:",cad2)
    print("Telefone",cad3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO clientes_fazenda (nome, email, telefone) VALUES (%s,%s,%s)"
    dados = (str(cad1),str(cad2),str(cad3))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    

app=QtWidgets.QApplication([])
cadastros=uic.loadUi("cadastro.ui")
cadastros.pushButton.clicked.connect(cadastro_clientes)

cadastros.show()
app.exec()