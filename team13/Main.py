from BPLUS_TUPLE import BPLUS_TUPLE


def Main():
    tree = BPLUS_TUPLE(3)

    tree.add(9)
    tree.add(3)
    tree.add(2)
    tree.add(1)
    tree.add(0)
    tree.add(15)
    tree.add(4)
    tree.add(16)
    tree.add(18)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(20)
    tree.add(25)
    tree.add(8)
    tree.showTree()

    print(tree.search(8))
    print(tree.search(10000))

    tree.graphTree()


Main()

# Test para funciones
def test():
    createDatabase('DB1')
    createDatabase('DB2')
    createDatabase('DB3')
    createDatabase('DB4')
    createDatabase('DB5')
    
    
    db2 = DataBase.buscar('DB2')
    # Insertando tablas a DB2
    db2.valor.insertar('DB2 - Valor1', 'T1')
    db2.valor.insertar('DB2 - Valor2', 'T2')
    db2.valor.insertar('DB2 - Valor3', 'T3')
    db2.valor.insertar('DB2 - Valor4', 'T4')
    db2.valor.insertar('DB2 - Valor5', 'T5')
    db2.valor.insertar('DB2 - Valor6', 'T6')
    
    db4 = DataBase.buscar('DB4')
    # Insertando tablas a DB4
    db4.valor.insertar('DB4 - Valor1', 'Estudiante')
    db4.valor.insertar('DB4 - Valor2', 'Profesor')
    db4.valor.insertar('DB4 - Valor3', 'Curso')
    db4.valor.insertar('DB4 - Valor4', 'Asignacion')
