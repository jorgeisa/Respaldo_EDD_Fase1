from BPLUS_TUPLE import BPLUS_TUPLE
from Funciones import showDatabases
from Funciones import *


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


# Test para funciones
def test():
    print("Creacion de DBs:")
    print(createDatabase('DB1'), end="-")
    print(createDatabase('DB2'), end="-")
    print(createDatabase('DB3'), end="-")
    print(createDatabase('DB4'), end="-")
    print(createDatabase('DB5'))
    print("Impresion de DBs:")
    print(showDatabases())

    # Graficando DBs
    DataBase.graficar()
    print("\nElimando la DB6:")
    print(dropDatabase('DB6'))
    DataBase.graficar()

    # Creando Tablas para DB2
    # createTable(database: str, table: str, numberColumns: int)
    print("\nCreacion de Tablas en DBs:")
    print("Creacion Tablas DB2:")
    print(createTable('DB2', 'Table1_DB2', [0, 2]), end="-")
    print(createTable('DB2', 'Table2_DB2', [0, 2]), end="-")
    print(createTable('DB2', 'Table3_DB2', [None, 2]), end="-")
    print(createTable('DB2', 'Table4_DB2', [0, 2]), end="-")
    print(createTable('DB2', 'Table5_DB2', [0, 2]), end="-")
    print(createTable('DB2', 'Table6_DB2', [0, 2]))

    # Creando tablas a DB4
    print("Creacion Tablas DB4:")
    print(createTable('DB4', 'Table1_DB4', [None, 4]), end="-")
    print(createTable('DB4', 'Table2_DB4', [0, 4]), end="-")
    print(createTable('DB4', 'Table3_DB4', [0, None]), end="-")
    print(createTable('DB4', 'Table4_DB4', [None, None]), end="-")
    print(createTable('DB4', 'Table5_DB4', [0, 4]), end="-")
    print(createTable('DB4', 'Table6_DB4', [0, 4]))

    # Mostrando las tablas
    # Mostrando Tablas DB2, DB3, DB4
    print("\nMostrando Tablas de DBs:")
    print("Tablas DB2:")
    print(showTables('DB2'))
    print("Tablas DB3 (sin tablas):")
    print(showTables('DB3'))
    print("Tablas DB30 (no existente):")
    print(showTables('DB30'))
    print("Tablas DB4:")
    print(showTables('DB4'))

    print("\nGraficando Tablas de DBs")
    print("Tablas de DB2")
    print(graficarTablas("DB2"))



# Main()
test()