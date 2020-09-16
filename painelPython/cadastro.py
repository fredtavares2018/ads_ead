from PyQt5 import QtWidgets, uic 

# importando o banco
import sqlite3

banco = sqlite3.connect('banco_cadastro.db')

def gravar():
    pegarNome = cadastro.digitar.text()
    pegarTelefone = cadastro.telefone.text()
    
    cursor = banco.cursor()
    cursor.execute(" CREATE TABLE IF NOT EXISTS usuarios (nome text, telefone text)")
    cursor.execute("INSERT INTO usuarios VALUES(?, ?)",(str(pegarNome),str(pegarTelefone)))
    banco.commit()
     
    #limpando input
    cadastro.digitar.setText("")
    cadastro.telefone.setText("")
    
def listar():
    listagemDados.show()
    
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM usuarios")
    receber_dados = cursor.fetchall()
    
    
    listagemDados.listagemBanco.setRowCount(len(receber_dados))
    listagemDados.listagemBanco.setColumnCount(2)
    
    for i in range(0, len(receber_dados)):
        for j in range(0, 2):
            listagemDados.listagemBanco.setItem(i,j, QtWidgets.QTableWidgetItem(str(receber_dados[i][j])))
    
    
    

app = QtWidgets.QApplication([])
# User Interface Compiler
cadastro = uic.loadUi('listagem.ui')
listagemDados = uic.loadUi('listaBanco.ui')

# ação dos botoes
cadastro.botaoCadastrar.clicked.connect(gravar)
cadastro.verCadastros.clicked.connect(listar)

cadastro.show()
app.exec()