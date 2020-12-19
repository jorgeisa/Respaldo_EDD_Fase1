#################### DILAN  ############################
from os import name
import re
from AVL_DB import AVL_DB as AvlDb
from AVL_TABLE import AVL_TABLE as AvlT
from BPLUS_TUPLE import BPLUS_TUPLE as bPlusT

DataBase = AvlDb()

#################### KEVIN ############################
pattern = r'[_]*[A-Za-z]+[_]*[_0-9]*[_]*'


#################### DILAN ############################
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


#################### DILAN ############################
def showDatabases():
    bases = DataBase.recorrido()
    lista = bases.split(' ')
    lista.pop()
    return lista


#################### KEVIN ############################
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


#################### ISAAC ############################
def dropDatabase(database):
    try:
        if re.match(pattern, database):
            dataB = DataBase.buscar(str(database))
            if dataB is None:
                return 2
            else:
                DataBase.eliminarDB(database)
                return 0
        else:
            return 1
    except:
        return 1


#################### ISAAC ############################
def createTable(database, table, numberColumns):
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is not None:
            tablaBuscada = dataB.avlTable.buscar(table)
            if tablaBuscada is None:
                bPlus = bPlusT(5, numberColumns)
                dataB.avlTable.insertar(bPlus, table, numberColumns)
                return 0
            return 3
        return 2
    except:
        return 1


#################### ISAAC ############################
def showTables(database):
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is not None:
            tablas = dataB.avlTable.recorrido()
            if not (len(tablas) == 0):
                listaTablas = tablas.split(' ')
                listaTablas.pop()
                return listaTablas
            return tablas
        return dataB
    except:
        return None


#################### DILAN ############################
def extractTable(database, table):
    try:
        BaseDatos = DataBase.buscar(database)
        if BaseDatos != None:
            Tabla = BaseDatos.avlTable.buscar(table)
            if Tabla != None:
                return Tabla.bPlus.extractReg()
        else:
            return None
    except:
        return None


#################### DILAN ############################
def extractRangeTable(database, table, columnNumber, lower, upper):
    try:
        BaseDatos = DataBase.buscar(database)
        if BaseDatos != None:
            Tabla = BaseDatos.avlTable.buscar(table)
            if Tabla != None:
                return Tabla.bPlus.extractRegRange(columnNumber, lower, upper)
        else:
            return None
    except:
        return None


#################### ISAAC############################
def alterAddPK(database, table, columns):
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is None:
            return 2
        tabla = dataB.avlTable.buscar(table)
        if tabla is None:
            return 3
        if not tabla.verifyListPk():
            return 4
        if not tabla.verifyColumns(columns):
            return 5
        return tabla.alterAddPk(columns)
    except:
        return 1


#################### ISAAC ############################
def alterDropPK(database, table):
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is None:
            return 2
        tabla = dataB.avlTable.buscar(table)
        if tabla is None:
            return 3
        if tabla.verifyListPk():
            return 4
        return tabla.alterDropPk()
    except:
        return 1


#################### KEVIN ############################
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


#################### KEVIN ############################
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


#################### ISAAC ############################
def alterDropColumn(database, table, columnNumber):
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is None:
            return 2
        tabla = dataB.avlTable.buscar(str(table))
        if tabla is None:
            return 3
        if tabla.verifyColumnPk(columnNumber):
            return 4
        if tabla.verifyOutOfRange(columnNumber):
            return 5
        contador = tabla.numberColumns
        tabla.numberColumns = contador - 1
        return tabla.bPlus.alterDropColumn(columnNumber)
    except:
        return 1


#################### KEVIN ############################
def dropTable(database, table):
    BaseDatos = DataBase.buscar(database)
    Tabla = BaseDatos.avlTable.buscar(table)
    if Tabla != None:
        BaseDatos.avlTable.eliminar(table)
        return 0
    elif Tabla == None:
        return 2
    return 1


#################### JORGE ############################
def insert(database, table, register):
    try:
        base = DataBase.buscar(str(database))
        if base is not None:
            tabla = base.avlTable.buscar(table)
            if tabla is not None:
                return tabla.bPlus.insert(register)
            return 3
        return 2
    except:
        return 1


#################### JORGE ############################
def loadCSV(file, database, table):
    try:
        base = DataBase.buscar(str(database))
        if base is not None:
            tabla = base.avlTable.buscar(table)
            if tabla is not None:
                results = []
                registers = file.split('\n')
                for i in registers:
                    register = i.split(',')
                    results.append(tabla.bPlus.insert(register))
                return results
            return [3]
        return [2]
    except:
        return [1]


#################### JORGE ############################
def extractRow(database, table, columns):
    try:
        base = DataBase.buscar(str(database))
        if base is not None:
            tabla = base.avlTable.buscar(table)
            if tabla is not None:
                return tabla.bPlus.extractRow(columns)
            return []
        return []
    except:
        return []


#################### JORGE ############################
def update(database, table, register, columns):
    try:
        base = DataBase.buscar(str(database))
        if base is not None:
            tabla = base.avlTable.buscar(table)
            if tabla is not None:
                return tabla.bPlus.update(register, columns)
            return 3
        return 2
    except:
        return 1


#################### JORGE ############################
def truncate(database, table):
    try:
        base = DataBase.buscar(str(database))
        if base is not None:
            tabla = base.avlTable.buscar(table)
            if tabla is not None:
                return tabla.bPlus.truncate()
            return 3
        return 2
    except:
        return 1


# FUNCIONALIDADES APARTE

#################### NO AGREGAR ############################
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
