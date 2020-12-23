import Funciones as tytus

print(tytus.createDatabase("db1"))  #0
print(tytus.createDatabase("db2"))  #0

print(tytus.createTable("db1", "profesor", 3))  #0
print(tytus.createTable("db1", "estudiantes", 2))   #0
print(tytus.createTable("db1", "cursos", 3))    #0

print(tytus.alterTable("db1", "profesor", "profesores"))    #0

print(tytus.alterAddPK("db1", "profesores", [2]))   #0

print(tytus.insert("db1", "profesores", [3, "Tacos", "0104"]))  #0
print(tytus.insert("db1", "profesores", [4, "Tacos2", "0103"])) #0
print(tytus.insert("db1", "profesores", [1, "Tacos3", "0104"])) #4
print(tytus.alterAddPK("db1", "profesores", [1, 2]))    #4
print(tytus.insert("db1", "profesores", [2, "Tampico", "0107"]))  #0  
print(tytus.insert("db1", "profesores", [5, "Tamaño", "0174"])) #0
print(tytus.alterDropPK("db1", "profesores"))   #0
print(tytus.alterAddPK("db1", "profesores", [0]))   #0
print(tytus.insert("db1", "profesores", [6, "Taco", "0109"]))   #0
print(tytus.insert("db1", "profesores", [7, "Tortilla", "0105"]))   #0
print(tytus.insert("db1", "profesores", [8, "Lucas", "0113"]))  #0
print(tytus.update("db1", "profesores", {1: "Gringa", 2: "0198"}, [8])) #0
print(tytus.alterDropColumn("db1", "profesores", 2))    #0
print(tytus.insert("db1", "profesores", [54, "Tuco"]))  #0
print(tytus.alterAddColumn("db1", "profesores", "Nueva Columna"))   #0

print(tytus.showDatabases())    #['db1', 'db2']
print(tytus.showTables("db1"))  #['profesores', 'estudiantes', 'cursos']

print(tytus.extractTable("db1","profesores"))
print()
print(tytus.extractRangeTable("db1","profesores",1,"Ta","o")) #Tampico, Tamaño, Taco

tytus.graficarTablas("db1")
