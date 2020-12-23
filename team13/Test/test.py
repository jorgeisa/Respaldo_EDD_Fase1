import Funciones as t

# print(t.dropAll())

print(t.createDatabase("universidad"))  #0
print(t.createDatabase("colegio"))  #0
print(t.createDatabase("colegio"))  #2
print(t.createDatabase(45)) #1
print(t.createDatabase("otraDB"))   #0
print(t.dropDatabase("otraDB")) #0
print(t.alterDatabase("colegio", "hospital"))   #0
print(t.dropDatabase("otraDB")) #2
print(t.alterDatabase("colegio", "colegio2"))   #2
print(t.showDatabases()) # ["universidad", "hospital"]

print(t.createTable("universidad", "profesores", 3))    #0
print(t.createTable("universidad", "estudiantes", 3))   #0
print(t.createTable("universidad", "cursos", 5))    #0
print(t.createTable("hospital", "doctores", 3)) #0
print(t.createTable("hospital", "enfermeros", 3)) #0
print(t.createTable("hospital", "medicinas", 3)) #0
print(t.createTable("hospital", "medicinas", 4)) #3
print(t.alterTable("hospital", "medicin", "medicina")) #3
print(t.alterTable("hospital", "medicinas", "doctores")) #4
print(t.alterTable("hospital", "medicinas", "medicina")) #0
print(t.dropTable("hospital", "enfermeros")) #0

print(t.showTables("db3"))  #None
print(t.showTables("universidad"))  #["profesores", "estudiantes", "cursos"]
print(t.showTables("colegio"))  #None
print(t.showTables("hospital")) #["doctores", "medicina"]

print(t.alterAddPK("universidad", "profesores", [0]))   #0
print(t.alterAddPK("universidad", "cursos", [0, 4]))    #0
print(t.alterAddPK("universidad", "estudiantes", 3))    #1
print(t.alterAddPK("universidad", "profesores", [1]))   #4
print(t.alterAddPK("universidad", "profesores", [3]))   #5
print(t.alterAddPK("universidad", "profesores", [0, 1, 2, 5]))   #5

# print(t.loadCSV("profesores.csv", "universidad", "profesores"))
print(t.loadCSV("C:\\Users\\Isaac\\Desktop\\test\\Daniel\\estudiantes.csv", "universidad", "estudiantes"))

print(t.alterAddPK("universidad", "estudiantes", [0]))

print(t.extractRow("universidad", "estudiantes", [1]))
print()
print(t.extractRow("universidad", "estudiantes", [3]))
print()
print(t.extractTable("universidad", "profesores"))
print()
print(t.extractRangeTable("universidad", "estudiantes", 0, 5, 10))
