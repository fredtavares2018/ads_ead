from PyQt5 import QtWidgets, uic 

def gravar():
    pegarNome = cadastro.lineEdit.text()
    #print('Você digitou', pegarNome)
    
    #abaixo você adiciona os nomes no ListWidget
    cadastro.lista.addItem(pegarNome)
    
    #limpando input
    cadastro.lineEdit.setText("")


app = QtWidgets.QApplication([])
# User Interface Compiler
cadastro = uic.loadUi('painelPython/cad.ui')

# ação dos botoes
cadastro.pushButton.clicked.connect(gravar)

cadastro.show()
app.exec()