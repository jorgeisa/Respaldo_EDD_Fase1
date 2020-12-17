import os


class BPLUS_TUPLE:
    
    def __init__(self, grade, size):
        if grade < 3 or grade is None or grade == "" or int(grade) < 3:
            self.__grade = 3
        else:
            self.__grade = grade

        self.__root = None
        self.__size = size
        self.__PK = []
        self.contador = 1
        self.hide = False
    
    def get_root(self):
        return self.__root
    
    def set_root(self, root):
        self.__root = root
        
    def set_PK(self, pk):
        self.__PK = pk
        self.hide = False
    
    def get_PK(self, pk):
        return self.__PK
    
    def insert(self, register: list) -> int:
        if self.__root is None:
            if len(register) == self.__size:
                self.__root = PageTBPlus(self.__grade)
                pk = []
                if self.__PK:
                    for i in self.__PK:
                        if type(register[i]) is str:
                            pk.append(register[i])
                        else: 
                            pk.append(str(register[i]))
                    if type(pk) is list:
                        pk = '-'.join(pk)
                else:
                    self.hide = True
                    pk = self.contador
                    self.contador += 1
                self.__root = self.__root.add_key(NodeTBPlus(pk,register))
                print(" -> 0")
                return 0
            else:
                print("Columnas Fuera De Limite -> 5")
                return 5
        else:
            if len(register) == self.__size:
                pk = []
                if self.__PK:
                    for i in self.__PK:
                        if type(register[i]) is str:
                            pk.append(register[i])
                        else:
                            pk.append(str(register[i]))
                    if type(pk) is list:
                        pk = '-'.join(pk)
                elif self.hide:
                    pk = self.contador
                    self.contador += 1
                else:
                    pass
                if self.Search(pk):
                    print(" -> 4")
                    return 4
                else:
                    self.__root = self.__root.add_key(NodeTBPlus(pk,register))
                    print(" -> 0")
                    return 0
            else:
                print("Columnas Fuera De Limite -> 5")
                return 5
    
    def loadCSV(self, file: str) -> list:
        results = []
        registers = file.split('\n')
        for i in registers:
            register = i.split(',')
            results.append(self.insert(register))
        return results

    def extractRow(self, columns: list) -> list:
       if self.__root is not None:
            pk = []
            for i in columns:
                if type(i) is str:
                    pk.append(i)
                elif (type(i) is int) and (len(columns) == 1):
                    pk = i
                else: 
                    pk.append(str(i))
            if type(pk) is list:
                pk = '-'.join(pk)
            if self.__root is not None:
                return self.__root._CallPage(pk)
       else:
            return []
    
    def update(self, register: dict, columns: list) -> int:
        if self.__root is not None:
            for column in register:
                if int(column) in self.__PK:
                    print(" -> 1")
                    return 1
            if len(register) > len(self.__PK):
                print(" -> 1")
                return 1
            pk = []
            for i in columns:
                if type(i) is str:
                    pk.append(i)
                elif type(i is int) and (len(self.__PK) == 1):
                    pk = i
                else: 
                    pk.append(str(i))
            if type(pk) is list:
                pk = '-'.join(pk)
            tupla = self.__root._CallPage(pk)
            if tupla:
                for column in register:
                    tupla[int(column)] = register[column]
                print(" -> 0")
                return 0
            else:
                print(" -> 4")
                return 4
        else:
            print(" -> 1")
            return 1
    
    def truncate(self) -> int:
        self.__root = None
        print(" -> 0")
        return 0
    
    def Search(self, key):
        if self.__root is not None:
            return self.__root.CallPage(key)
    
    # Print tree
    def showTree(self):
        self._showTree(self.__root, 0)

    def _showTree(self, tmp, level):
        print("Level", level, ": ", end="")
        tmp.showKeys()
        if not (len(tmp.get_chlds()) == 0):
            for i in range(len(tmp.get_chlds())):
                self._showTree(tmp.get_chlds()[i], level + 1)

    # graph tree
    def graphTree(self):
        if self.__root is not None:
            graph = 'digraph G{\n'
            graph += "node[shape = \"record\"]\n"
            graph += self._graphTree(self.__root, 0)
            graph += "{rank=same;\n"
            graph += self._rankLeaves(self.__root)
            graph += "}"
            graph += '}'
            file = open("ArbolB+.dot", "w")
            file.write(graph)
            file.close()
            os.system('dot -Tpng ArbolB+.dot -o ArbolB+.png')
        else:
            print("No hay Tuplas")

    def _graphTree(self, tmp, level):
        cadena = ""
        cadena += tmp.graphKeys(tmp, level)
        if not (len(tmp.get_chlds()) == 0):
            for i in range(len(tmp.get_chlds())):
                cadena += self._graphTree(tmp.get_chlds()[i], level + 1)
        return cadena
                
    # Rank = same to the nodes (leaves)
    def _rankLeaves(self, tmp):
        cadena = ""
        cadena += tmp.rankLeavesKeys(tmp)
        return cadena
    
    def alterAddColumn(self, new_column):
        contador = 0
        self._alterAddColumn(self.__root, new_column, contador)
        self.__size += 1
        print('NUEVO TAMAÑO DE LA TABLA: ', self.__size)

    def _alterAddColumn(self, temp, new_column, contador):
        temp.add_new_column(temp, new_column, contador)

        
class PageTBPlus:
    
    def __init__(self, grade):
        if grade < 3:
            self.__grade = 3
        else:
            self.__grade = grade

        self.__keys = []
        self.__childs = []
        self.__father = None
        self.__next = None
        self.__previous = None

    def get_keys(self):
        return self.__keys
    
    def get_chlds(self):
        return self.__childs
    
    def get_father(self):
        return self.__father
    
    def get_grade(self):
        return self.__grade
    
    def get_next(self):
        return self.__next
    
    def get_previous(self):
        return self.__previous
    
    def set_keys(self, keys):
        self.__keys = keys
    
    def set_chlds(self, childs):
        self.__childs = childs
    
    def set_father(self, father):
        self.__father = father
    
    def set_grade(self, grade):
        self.__grade = grade
    
    def set_next(self, next):
        self.__next = next
    
    def set_previous(self, previous):
        self.__previous = previous

    def add_chld(self, chld):
        self.__childs.append(chld)
    
    def add_key(self, key):
        if len(self.__keys) == 0:
            self.__keys.append(key)
            return self
        else:
            if len(self.__childs) == 0:
                self.sort(key)
                if len(self.__keys) == (self.__grade):
                     return self.SplitPage()
                return self
            else:
                i = 0
                if key.value < self.__keys[i].value:
                    aux = self.__childs[i].add_key(key)
                    return self.insert_childs(aux, i)                   

                elif (self.__keys[i].value < key.value) and (len(self.__keys) == 1):
                    aux = self.__childs[i + 1].add_key(key)
                    return self.insert_childs(aux, (i + 1))

                while i < (len(self.__keys) - 1):
                    if (self.__keys[i].value < key.value) and (key.value < self.__keys[i + 1].value):
                        aux = self.__childs[i + 1].add_key(key)
                        return self.insert_childs(aux, (i + 1))
                    i += 1
                    
                i += 1
                if self.__keys[i - 1].value < key.value:
                    aux = self.__childs[i].add_key(key)
                    return self.insert_childs(aux, i)

    def SplitPage(self):
        if (self.__grade % 2) > 0:
            index = int((self.__grade - 1) /2)
        else:
            index = int(self.__grade / 2)
        
        chld1 = PageTBPlus(self.__grade)
        chld2 = PageTBPlus(self.__grade)

        if (self.__father is None) and (len(self.__childs) == 0):
            temp = PageTBPlus(self.__grade)
            temp.add_key(self.__keys[index])

            for i in range(len(self.__keys)):
                if i < index:
                    chld1.__keys.append(self.__keys[i])
                else:
                    chld2.__keys.append(self.__keys[i])

            temp.add_chld(chld1)
            temp.add_chld(chld2)
            chld1.__father = temp
            chld2.__father = temp
            temp.__father = self.__father
            auxiliar = self.__previous
            if auxiliar is not None: 
                auxiliar.__next = chld1
            chld1.__previous = auxiliar
            chld1.__next = chld2
            chld2.__previous = chld1
            chld2.__next = self.__next
            if self.__next is not None:
                self.__next.__previous = chld2
            return temp

        elif len(self.__childs) == 0:
            for i in range(len(self.__keys)):
                if i < index:
                    chld1.__keys.append(self.__keys[i])
                else:
                    chld2.__keys.append(self.__keys[i])

            chld1.__father = self.__father
            chld2.__father = self.__father
            auxiliar = self.__previous
            if auxiliar is not None: 
                auxiliar.__next = chld1
            chld1.__previous = auxiliar
            chld1.__next = chld2
            chld2.__previous = chld1
            chld2.__next = self.__next
            if self.__next is not None:
                self.__next.__previous = chld2
            temp = []
            temp.extend([chld1, chld2, self.__keys[index]])
            return temp
        else:
            if self.__father is not None:
                if len(self.__father.__keys) < self.__grade:
                    for i in range(len(self.__keys)):
                        if i < index:
                            chld1.__keys.append(self.__keys[i])
                        elif i > index:
                            chld2.__keys.append(self.__keys[i])

                    for i in range(len(self.__childs)):
                        aux = self.__childs[i]
                        if i <= index:
                            chld1.add_chld(aux)
                            aux.__father = chld1
                        else:
                            chld2.add_chld(aux)
                            aux.__father = chld2
                    
                    chld1.__father = self.__father
                    chld2.__father = self.__father
                    temp = []
                    temp.extend([chld1, chld2, self.__keys[index]])
                    return temp
            else:
                temp = PageTBPlus(self.__grade)
                temp.add_key(self.__keys[index])

                for i in range(len(self.__keys)):
                    if i < index:
                        chld1.__keys.append(self.__keys[i])
                    elif i > index:
                        chld2.__keys.append(self.__keys[i])

                for i in range(len(self.__childs)):
                    aux = self.__childs[i]
                    if i <= index:
                        chld1.add_chld(aux)
                        aux.__father = chld1
                    else:
                        chld2.add_chld(aux)
                        aux.__father = chld2

                temp.add_chld(chld1)
                temp.add_chld(chld2)
                chld1.__father = temp
                chld2.__father = temp
                return temp

    def sort(self, key):
        for i in range(len(self.__keys)):
            if key.value < self.__keys[i].value:
                self.__keys.insert(i,key)
                break
            elif i == (len(self.__keys) - 1):
                self.__keys.append(key)
    
    def insert_childs(self, aux, i):
        if type(aux) is list:
            self.__childs.pop(i)
            for x in range(len(aux) - 1):
                self.__childs.insert((i + x), aux[x])
            if len(self.__keys) < self.__grade:
                self.sort(aux[len(aux) - 1])
                if len(self.__keys) == (self.__grade):
                    return self.SplitPage()
                return self
            else:
                self.add_key(aux[len(aux) - 1])
        else:
            self.__childs[i] = aux
        return self
    
    def CallPage(self, key):
        if (len(self.__childs) == 0) and (self.__father is None):
            return self.SearchTuple(key)
        elif len(self.__childs) == 0:
            return self.SearchTuple(key)
        else:
            return self.__childs[0].CallPage(key)

    def SearchTuple(self, key):
        if self is not None:
            for i in self.__keys:
                if i.value == key:
                    return True
            if self.__next is None:
                return False
            else:
                return self.__next.SearchTuple(key)
    
    def _CallPage(self, key):
        if (len(self.__childs) == 0) and (self.__father is None):
            return self._SearchTuple(key)
        elif len(self.__childs) == 0:
            return self._SearchTuple(key)
        else:
             return self.__childs[0]._CallPage(key)

    def _SearchTuple(self, key):
        if self is not None:
            for i in self.__keys:
                if i.value == key:
                    return i.register
            if self.__next is None:
                return []
            else:
                return self.__next._SearchTuple(key)

    # Show Keys of Page
    def showKeys(self):
        if not (len(self.__keys) == 0):
            print("[", end=" ")
            for i in range(len(self.__keys)):
                print(self.__keys[i].value, ",", end=" ")
            print("]", end=" ")
            if not (self.__next is None):
                print("[ ", end="")
                for i in range(len(self.__next.__keys)):
                    print(self.__next.__keys[i].value, end=" ")
                print("]", end="")
            else:
                pass
        contador = 0
        if not (len(self.__childs) == 0):
            for x in range(len(self.__childs)):
                contador += 1
        print(" contador hijos: ", contador)

    # Graph and show keys
    def graphKeys(self, tmp, level):
        cadena = ""
        if not (len(self.__keys) == 0):
            keysString = ""
            if level != 0:
                for i in range(len(self.__keys)):
                    if not (i == (len(self.__keys) - 1)):
                        keysString += f"{self.__keys[i].value}, "
                    else:
                        keysString += f"{self.__keys[i].value}"
                cadena += f"{tmp} [label=\"{keysString}\" color=red]\n"

                if len(self.__childs) != 0:
                    for i in range(len(self.__childs)):
                        cadena += f"{tmp} -> {self.__childs[i]}\n"

                if not (self.__next is None):
                    cadena += f"{tmp} -> {self.__next}\n"

            else:
                for i in range(len(self.__keys)):
                    if not (i == (len(self.__keys) - 1)):
                        keysString += f"{self.__keys[i].value}, "
                    else:
                        keysString += f"{self.__keys[i].value}"
                cadena += f"{tmp} [label=\"{keysString}\" color=green]\n"

                if len(self.__childs) != 0:
                    for i in range(len(self.__childs)):
                        cadena += f"{tmp} -> {self.__childs[i]}\n"
        return cadena
                        
    # Rank = same to the nodes (leaves)
    def rankLeavesKeys(self, tmp):
        cadena = ""
        if len(tmp.get_chlds()) != 0:
            cadena += self.rankLeavesKeys(tmp.get_chlds()[0])
        else:
            cadena += f"{tmp};\n"
            if tmp.get_next() is not None:
                cadena += self.rankLeavesKeys(tmp.get_next())
        return cadena
    
    # Metodo para agregar nueva columna a la tabla
    def add_new_column(self, temp, new_column, contador):
        if len(temp.get_chlds()) != 0:
            self.add_new_column(temp.get_chlds()[0], new_column, contador)
        else:
            for i in temp.get_keys():
                i.register.append(new_column)

            if temp.get_next() is not None:
                self.add_new_column(temp.get_next(), new_column, contador)    

                
class NodeTBPlus:

    def __init__(self, PK, register):
        self.value = PK
        self.register = register
        


    
