from BPLUS_TUPLE import BPLUS_TUPLE
from Funciones import showDatabases
from Funciones import *


def Main():
    tree = BPLUS_TUPLE(3, 2)

    tree.insert([1, "A"])
    tree.insert([2, "B"])
    tree.insert([3, "C"])
    tree.insert([4, "D"])
    tree.insert([5, "E"])
    tree.insert([6, "F"])
    tree.insert([7, "G"])
    tree.insert([8, "H"])

    # Mostrando registros
    print(tree.extractRow([1]))
    print(tree.extractRow([2]))
    print(tree.extractRow([3]))
    print(tree.extractRow([4]))
    print(tree.extractRow([5]))
    print(tree.extractRow([6]))
    print(tree.extractRow([7]))
    print(tree.extractRow([8]))


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

    print('\nInsertando tuplas en DB4:')
    print(insert('DB4', 'Table1_DB4', [1, "Manuel"]), end='-')
    print(insert('DB4', 'Table1_DB4', [2, "Gabriela"]), end='-')
    print(insert('DB4', 'Table1_DB4', [3, "Diego"]), end='-')
    print(insert('DB4', 'Table1_DB4', [4, "Diego"]))

    print('Colocando las llaves primarias con alter')
    print(alterAddPK('DB4', 'Table1_DB4', [1]))
    # print("\nGraficando Tablas de DBs")
    # print("Tablas de DB2")
    # print(graficarTablas("DB2"))



Main()
# test()
