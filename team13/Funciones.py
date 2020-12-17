from os import name
import re
from AVL_DB import AVL_DB as AvlDb
from AVL_TABLE import AVL_TABLE as AvlT
from BPLUS_TUPLE import BPLUS_TUPLE as bPlusT

DataBase = AvlDb()
pattern = r'[_]*[A-Za-z]+[_]*[_0-9]*[_]*'


def createDatabase(nameDb):
    if re.match(pattern, nameDb):
        busqueda = DataBase.buscar(str(nameDb))
        if busqueda == None:
            tabla = AvlT()
            DataBase.insertar(tabla, nameDb)
            return 0
        elif busqueda != None:
            return 2  
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


def createTable(database, table, numberColumns):
    dataB = DataBase.buscar(str(database))
    if dataB is not None:
        tablaBuscada = dataB.avlTable.buscar(table)
        if tablaBuscada is None:
            bPlus = bPlusT(5, numberColumns)
            dataB.avlTable.insertar(bPlus, table, numberColumns)
            return 0
        return 3
    return 2


def showTables(database):
    dataB = DataBase.buscar(str(database))
    if dataB is not None:
        tablas = dataB.avlTable.recorrido()
        if not (len(tablas) == 0):
            listaTablas = tablas.split(' ')
            listaTablas.pop()
            return listaTablas
        return tablas
    return dataB


def alterTable(database, tableOld, tableNew):
    try:
        if re.match(pattern, database):
            db = DataBase.buscar(database)
            if db is None:
                return 2
            else:
                table = db.avlTable.buscar(tableOld)
                table_new = db.avlTable.buscar(tableNew)

                if table is None:
                    return 3
                elif table_new is not None:
                    return 4
                else:
                    if table is not None:
                        if db.avlTable.actualizar(tableOld, tableNew) == 'exito':
                            return 0
        else:
            return 1
    except:
        return 1
    
def alterAddColumn(database, table, default):
    try:
        db = DataBase.buscar(str(database))
        if db is None:
            return 2
        else:
            tabla = db.avlTable.buscar(table)
            if tabla is None:
                return 3
            else:
                tabla.bPlus.alterAddColumn(default)
                return 0
    except:
        return 1    

    
def dropTable(database,table):
    BaseDatos = DataBase.buscar(database)
    Tabla = BaseDatos.avlTable.buscar(table)
    if Tabla != None:
        BaseDatos.avlTable.eliminar(table)
        return 0
    elif Tabla == None:
        return 2
    return 1

def insert(database, table, register):
    try:
        base = DataBase.buscar(str(database))
        if base is None:
            return 2
        else:
            tabla = base.avlTable.buscar(table)
            if tabla is None:
                return 3
            else:
                return tabla.bPlus.insert(register)
    except:
        return 1

def loadCSV(file, database, table):
    try:
        results = []
        base = DataBase.buscar(str(database))
        if base is None:
            return results.append(2)
        else:
            tabla = base.avlTable.buscar(table)
            if tabla is None:
                return results.append(3)
            else:
                registers = file.split('\n')
                for i in registers:
                    register = i.split(',')
                    results.append(tabla.bPlus.insert(register))
                return results
    except:
        return []

def extractRow(database, table, columns):
    try:
        base = DataBase.buscar(str(database))
        if base is None:
            return 2
        else: 
            tabla = base.avlTable.buscar(table)
            if tabla is None:
                return 3
            else:
                return tabla.bPlus.extractRow(columns)

    except:
        return []

def update(database, table, register, columns):
    try:
        base = DataBase.buscar(str(database))
        if base is None:
            return 2
        else:
            tabla =  base.avlTable.buscar(table)
            if tabla is None:
                return 3
            else:
                return tabla.bPlus.update(register, columns)
    except:
        return 1

def truncate(database, table):
    try:
        base = DataBase.buscar(str(database))
        if base is None:
            return 2
        else:
            tabla = base.avlTable.buscar(table)
            if tabla is None:
                return 3
            else:
                return tabla.bPlus.truncate()
    except:
        return 1


# FUNCIONALIDADES APARTE


def graficarTablas(database):
    dataB = DataBase.buscar(database)
    if dataB is None:
        return dataB
    else:
        avl = dataB.avlTable
        if avl.raiz is not None:
            avl.graficar()
            return 1
        return avl
