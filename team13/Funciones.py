from os import name
import re
from AVL_DB import AVL_DB as AvlDb
from AVL_TABLE import AVL_TABLE as AvlT

DataBase = AvlDb()
pattern = r'[_]*[A-Za-z]+[_]*[_0-9]*[_]*'


def createDatabase(nameDb):
    busqueda = DataBase.buscar(str(nameDb))
    if busqueda == None:
        tabla = AvlT()
        DataBase.insertar(tabla, nameDb)
        return 0
    elif busqueda != None:
        return 2
    else:
        return 1


def showDatabases():
    bases = DataBase.recorrido()
    lista = bases.split(' ')
    lista.pop()
    return lista


def alterDatabase(databaseOld, databaseNew):
    if (re.match(pattern, databaseOld)) and (re.match(pattern, databaseNew)):
        db = DataBase.buscar(str(databaseOld))
        db_new = DataBase.buscar(str(databaseNew))

        if db is None:
            return 2
        elif db_new is not None:
            return 3
        else:
            if db is not None:
                if DataBase.actualizar(databaseOld, databaseNew) == 'exito':
                    return 0
                else:
                    return 1
    else:
        return 1


def dropDatabase(database):
    if re.match(pattern, database):
        dataB = DataBase.buscar(str(database))
        if dataB is None:
            return 2
        else:
            DataBase.eliminarDB(database)
            return 0
    else:
        return 1


def alterTable(database, tableOld, tableNew):
    if re.match(pattern, database):
        db = DataBase.buscar(database)
        table = db.valor.buscar(tableOld)
        tabla_new = db.valor.buscar(tableNew)

        if db is None:
            return 2
        elif table is None:
            return 3
        elif tabla_new is not None:
            return 4
        else:
            if table is not None:
                if db.valor.actualizar(tableOld, tableNew) == 'exito':
                    return 0
                else:
                    return 1
    else:
        return 1
