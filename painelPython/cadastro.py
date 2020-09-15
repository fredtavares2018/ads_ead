from PyQt5 import QtWidgets, uic 

def gravar():
    pegarNome = cadastro.digitar.text()
    pegarTelefone = cadastro.telefone.text()
    #print('Você digitou', pegarNome)
    
    #abaixo você adiciona os nomes no ListWidget
    cadastro.listaCadastro.addItem("Nome: " + pegarNome + " Telefone: " + pegarTelefone)
    
    #limpando input
    cadastro.digitar.setText("")


app = QtWidgets.QApplication([])
# User Interface Compiler
cadastro = uic.loadUi('listagem.ui')

# ação dos botoes
cadastro.botaoCadastrar.clicked.connect(gravar)

cadastro.show()
app.exec()