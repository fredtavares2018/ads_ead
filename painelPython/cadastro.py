from PyQt5 import QtWidgets, uic 

def gravar():
    pegarNome = cadastro.lineEdit.text()
    print('Você digitou', pegarNome)


app = QtWidgets.QApplication([])
# User Interface Compiler
cadastro = uic.loadUi('cad.ui')

# ação dos botoes
cadastro.pushButton.clicked.connect(gravar)

cadastro.show()
app.exec()