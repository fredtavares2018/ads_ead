from PyQt5 import  uic,QtWidgets, QtGui

nomesDigitados = []
def cadastro_clientes():
    
    cad1 = cadastros.lineEdit.text()
    
    # metodo para usar ListView
    
    nomesDigitados.append(cad1)                 # aqui incrementa nossa lista(array)
    model = QtGui.QStandardItemModel()
    cadastros.listView.setModel(model)
    for i in nomesDigitados:
        item = QtGui.QStandardItem(i)
        model.appendRow(item)

    
    cadastros.listWidget.addItem(str(cad1))
    
    # o melhor é usar com banco de dados
    
    cadastros.tableWidget.setRowCount(len(nomesDigitados))
    cadastros.tableWidget.setColumnCount(1)

    for i in range(0, len(nomesDigitados)):
        for j in range(0, 1):
            cadastros.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(nomesDigitados[i])))


    # aqui limpamos os campos do cadastro
    cadastros.lineEdit.setText("")



app=QtWidgets.QApplication([])
cadastros=uic.loadUi("testes.ui")
cadastros.pushButton.clicked.connect(cadastro_clientes)


cadastros.show()
app.exec()