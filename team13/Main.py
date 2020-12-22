from BPLUS_TUPLE import BPLUS_TUPLE
from Funciones import showDatabases
from Funciones import *
from timeit import default_timer
import Funciones as j



def Main():
    tree = BPLUS_TUPLE(3, 2)

    tree.j.insert([1, "A"])
    tree.j.insert([2, "B"])
    tree.j.insert([3, "C"])
    tree.j.insert([4, "D"])
    tree.j.insert([5, "E"])
    tree.j.insert([6, "F"])
    tree.j.insert([7, "G"])
    tree.j.insert([8, "H"])

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
    print(j.createDatabase('DB1'), end="-")
    print(j.createDatabase('DB2'), end="-")
    print(j.createDatabase('DB3'), end="-")
    print(j.createDatabase('DB4'), end="-")
    print(j.createDatabase('DB5'), end="-")
    print(j.createDatabase('DB6'), end="-")
    print(j.createDatabase('DB7'), end="-")
    print(j.createDatabase('DB8'), end="-")
    print(j.createDatabase('DB9'), end="-")
    print(j.createDatabase('DB10'), end="-")
    print(j.createDatabase('DB11'), end="-")
    print(j.createDatabase('DB12'), end="-")
    print(j.createDatabase('DB13'), end="-")
    print(j.createDatabase('DB14'), end="-")
    print(j.createDatabase('DB15'), end="-")


    print(j.createDatabase('DB16'), end="-")
    print(j.createDatabase('DB17'), end="-")
    print(j.createDatabase('DB18'), end="-")
    print(j.createDatabase('DB19'), end="-")
    print(j.createDatabase('DB20'), end="-")
    print(j.createDatabase('DB21'), end="-")
    print(j.createDatabase('DB22'), end="-")
    print(j.createDatabase('DB23'), end="-")
    print(j.createDatabase('DB24'), end="-")
    print(j.createDatabase('DB25'))
    print(j.createDatabase('DB26'), end="-")
    print(j.createDatabase('DB27'), end="-")
    print(j.createDatabase('DB28'), end="-")
    print(j.createDatabase('DB29'), end="-")
    print(j.createDatabase('DB30'), end="-")
    print(j.createDatabase('DB31'), end="-")
    print(j.createDatabase('DB32'), end="-")
    print(j.createDatabase('DB33'), end="-")
    print(j.createDatabase('DB34'), end="-")
    print(j.createDatabase('DB35'), end="-")
    print(j.createDatabase('DB36'), end="-")
    print(j.createDatabase('DB37'), end="-")
    print(j.createDatabase('DB38'), end="-")
    print(j.createDatabase('DB39'), end="-")
    print(j.createDatabase('DB40'), end="-")
    print(j.createDatabase('DB41'), end="-")
    print(j.createDatabase('DB42'), end="-")
    print(j.createDatabase('DB43'), end="-")
    print(j.createDatabase('DB44'), end="-")
    print(j.createDatabase('DB45'), end="-")
    print(j.createDatabase('DB46'), end="-")
    print(j.createDatabase('DB47'), end="-")
    print(j.createDatabase('DB48'), end="-")
    print(j.createDatabase('DB49'), end="-")
    print(j.createDatabase('DB50'))
    print(j.createDatabase('DB51'), end="-")
    print(j.createDatabase('DB52'), end="-")
    print(j.createDatabase('DB53'), end="-")
    print(j.createDatabase('DB54'), end="-")
    print(j.createDatabase('DB55'), end="-")
    print(j.createDatabase('DB56'), end="-")
    print(j.createDatabase('DB57'), end="-")
    print(j.createDatabase('DB58'), end="-")
    print(j.createDatabase('DB59'), end="-")
    print(j.createDatabase('DB60'), end="-")
    print(j.createDatabase('DB61'), end="-")
    print(j.createDatabase('DB62'), end="-")
    print(j.createDatabase('DB63'), end="-")
    print(j.createDatabase('DB64'), end="-")
    print(j.createDatabase('DB65'), end="-")
    print(j.createDatabase('DB66'), end="-")
    print(j.createDatabase('DB67'), end="-")
    print(j.createDatabase('DB68'), end="-")
    print(j.createDatabase('DB69'), end="-")
    print(j.createDatabase('DB70'), end="-")
    print(j.createDatabase('DB71'), end="-")
    print(j.createDatabase('DB72'), end="-")
    print(j.createDatabase('DB73'), end="-")
    print(j.createDatabase('DB74'), end="-")
    print(j.createDatabase('DB75'))
    print(j.createDatabase('DB76'), end="-")
    print(j.createDatabase('DB77'), end="-")
    print(j.createDatabase('DB78'), end="-")
    print(j.createDatabase('DB79'), end="-")
    print(j.createDatabase('DB80'), end="-")
    print(j.createDatabase('DB81'), end="-")
    print(j.createDatabase('DB82'), end="-")
    print(j.createDatabase('DB83'), end="-")
    print(j.createDatabase('DB84'), end="-")
    print(j.createDatabase('DB85'), end="-")
    print(j.createDatabase('DB86'), end="-")
    print(j.createDatabase('DB87'), end="-")
    print(j.createDatabase('DB88'), end="-")
    print(j.createDatabase('DB89'), end="-")
    print(j.createDatabase('DB90'), end="-")
    print(j.createDatabase('DB91'), end="-")
    print(j.createDatabase('DB92'), end="-")
    print(j.createDatabase('DB93'), end="-")
    print(j.createDatabase('DB94'), end="-")
    print(j.createDatabase('DB95'), end="-")
    print(j.createDatabase('DB96'), end="-")
    print(j.createDatabase('DB97'), end="-")
    print(j.createDatabase('DB98'), end="-")
    print(j.createDatabase('DB99'), end="-")
    print(j.createDatabase('DB100'))

    print("\nCreacion de Tablas en DBs:")
    print("Creacion Tablas DB2:")
    print(j.createTable('DB2', 'Table1_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table2_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table3_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table4_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table5_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table6_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table7_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table8_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table9_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table10_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table11_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table12_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table13_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table14_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table15_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table16_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table17_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table18_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table19_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table20_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table21_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table22_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table23_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table24_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table25_DB2', 2))
    print(j.createTable('DB2', 'Table26_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table27_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table28_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table29_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table30_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table31_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table32_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table33_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table34_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table35_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table36_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table37_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table38_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table39_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table40_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table41_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table42_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table43_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table44_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table45_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table46_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table47_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table48_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table49_DB2', 2), end="-")
    print(j.createTable('DB2', 'Table50_DB2', 2))

    # Creando tablas a DB4
    print("Creacion Tablas DB4:")
    print(j.createTable('DB4', 'Table1_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table2_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table3_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table4_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table5_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table6_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table7_DB4', 4), end="-")
    print(j.createTable('DB2', 'Table8_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table9_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table10_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table11_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table12_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table13_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table14_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table15_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table16_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table17_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table18_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table19_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table20_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table21_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table22_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table23_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table24_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table25_DB4', 4))
    print(j.createTable('DB4', 'Table26_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table27_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table28_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table29_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table30_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table31_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table32_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table33_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table34_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table35_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table36_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table37_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table38_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table39_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table40_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table41_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table42_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table43_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table44_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table45_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table46_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table47_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table48_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table49_DB4', 4), end="-")
    print(j.createTable('DB4', 'Table50_DB4', 4))

    print("Creacion Tablas DB6:")
    print(j.createTable('DB6', 'Table1_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table2_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table3_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table4_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table5_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table6_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table7_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table8_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table9_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table10_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table11_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table12_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table13_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table14_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table15_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table16_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table17_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table18_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table19_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table20_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table21_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table22_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table23_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table24_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table25_DB6', 6))
    print(j.createTable('DB6', 'Table26_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table27_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table28_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table29_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table30_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table31_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table32_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table33_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table34_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table35_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table36_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table37_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table38_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table39_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table40_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table41_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table42_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table43_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table44_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table45_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table46_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table47_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table48_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table49_DB6', 6), end="-")
    print(j.createTable('DB6', 'Table50_DB6', 6))

    print("Creacion Tablas DB8:")
    print(j.createTable('DB8', 'Table1_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table2_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table3_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table4_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table5_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table6_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table7_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table8_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table9_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table10_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table11_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table12_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table13_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table14_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table15_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table16_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table17_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table18_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table19_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table20_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table21_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table22_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table23_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table24_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table25_DB8', 8))
    print(j.createTable('DB8', 'Table26_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table27_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table28_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table29_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table30_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table31_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table32_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table33_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table34_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table35_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table36_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table37_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table38_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table39_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table40_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table41_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table42_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table43_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table44_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table45_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table46_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table47_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table48_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table49_DB8', 8), end="-")
    print(j.createTable('DB8', 'Table50_DB8', 8))

    print("Creacion Tablas DB10:")
    print(j.createTable('DB10', 'Table1_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table2_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table3_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table4_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table5_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table6_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table7_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table8_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table9_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table10_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table11_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table12_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table13_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table14_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table15_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table16_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table17_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table18_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table19_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table20_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table21_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table22_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table23_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table24_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table25_DB10', 10))
    print(j.createTable('DB10', 'Table26_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table27_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table28_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table29_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table30_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table31_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table32_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table33_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table34_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table35_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table36_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table37_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table38_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table39_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table40_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table41_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table42_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table43_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table44_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table45_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table46_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table47_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table48_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table49_DB10', 10), end="-")
    print(j.createTable('DB10', 'Table50_DB10', 10))

    print('\nj.insertando tuplas en DB4:')
    print(j.insert('DB4', 'Table1_DB4', [1, "Manuel", 0.5, "Azul"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [2, "Gabriela", 1.5, "Amarillo"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [3, "Diego", 2.5, "Verde"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [4, "Antonio", 3.5, "Rosado"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [5, "Jorge", 4.5, "Anaranjado"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [6, "Mynor", 5.5, "Gris"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [7, "Kevin", 6.5, "Celeste"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [8, "Aejandro", 7.5, "Blanco"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [9, "Nathan", 8.5, "Negro"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [10, "Jessica", 9.5, "Rojo"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [11, "Ericha", 10.5, "Azul"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [12, "Merry", 11.5, "Amarillo"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [13, "Sib", 12.5, "Verde"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [14, "Violetta", 13.5, "Rosado"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [15, "Meghan", 14.5, "Anaranjado"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [16, "Heinrick", 15.5, "Gris"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [17, "Tiler", 16.5, "Celeste"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [18, "Dennie", 17.5, "Blanco"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [19, "Dorie", 18.5, "Negro"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [20, "Niles", 19.5, "Rojo"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [21, "Olag", 20.5, "Azul"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [22, "Noland", 21.5, "Amarillo"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [23, "Paulita", 22.5, "Verde"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [24, "Forrest", 23.5, "Rosado"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [25, "Ulrick", 24.5, "Anaranjado"]))
    print(j.insert('DB4', 'Table1_DB4', [26, "Angil", 25.5, "Gris"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [27, "Fiona", 26.5, "Celeste"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [28, "Rodrick", 27.5, "Blanco"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [29, "Carolyne", 28.5, "Negro"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [30, "Cortney", 29.5, "Rojo"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [31, "Byron", 30.5, "Azul"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [32, "Lazarus", 31.5, "Amarillo"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [33, "Cyndy", 32.5, "Verde"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [34, "Becca", 33.5, "Rosado"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [35, "Brody", 34.5, "Anaranjado"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [36, "Darda", 35.5, "Gris"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [37, "Patrice", 36.5, "Celeste"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [38, "Bay", 37.5, "Blanco"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [39, "Giffy", 38.5, "Negro"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [40, "Hallsy", 39.5, "Rojo"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [41, "Elinor", 40.5, "Azul"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [42, "Maitilde", 41.5, "Amarillo"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [43, "Van", 42.5, "Verde"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [44, "Marcel", 43.5, "Rosado"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [45, "Giselle", 44.5, "Anaranjado"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [46, "Olympe", 45.5, "Gris"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [47, "Roxi", 46.5, "Celeste"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [48, "Debbi", 47.5, "Blanco"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [49, "Baron", 48.5, "Negro"]), end='-')
    print(j.insert('DB4', 'Table1_DB4', [50, "Debera", 49.5, "Rojo"]))


    print("Impresion 1")
    testShow('DB4', 'Table1_DB4')

    print("\nProbando j.alterDatabase: DB4")
    print(j.alterDatabase("DB4", "DB4P"), end='-')  # Caso bueno
    print(j.alterDatabase("DB4_Plus2", 7), end='-')  # error
    print(j.alterDatabase("DB4", "DB4_Plus"), end='-')  # no existe old
    print(j.alterDatabase("DB4_Plus", "DB5"))  # existe new


    print("\nImpresion 2:")
    testShow("DB4P", 'Table1_DB4')

    print('\nProbando j.dropDatabase:')
    print(j.dropDatabase('DB5'), end='-')
    # print(j.dropDatabase('DB4P'), end='-')
    print(j.dropDatabase('DB11'), end='-')  
    print(j.dropDatabase('@'), end='-')  # error
    print(j.dropDatabase('DB4_Plus8'))  # No existente

    print("\nProbando j.extractTable:")

    print(j.extractTable("DB4P", "Table1_DB4"))  # Lista de tuplas
    print(j.extractTable("DB4P", "Table2_DB4"), end="-")  # Lista vacia, sin tupla
    print(j.extractTable("DB4Pll", "Table2_DB4"), end="-")  # DB no existe
    print(j.extractTable("DB4P", "Table2_DB4ll"), end="-")  # Tabla no existe
    print(j.extractTable("DB4P", 1))  # Error

    print("\nImpresion 3:")
    testShow("DB4P", 'Table1_DB4')

    print("\nProbado el j.extractRangeTable:")
    print(j.extractRangeTable("DB4P", "Table1_DB4", 2, 22.5, 39.5))  # Existe valido
    print(j.extractRangeTable("DB4P", "Table2_DB4", 2, 22.5, 39.5), end="-")  # No existen tuplas
    print(j.extractRangeTable("DB4P", 1, 2, 22.5, 39.5))  # no existe base, tabla o error

    print("\nProbado el j.alterAddPK:")
    print(j.alterAddPK("DB4P", "Table1_DB4", [0, 5]), end='-')  # Columna fuera de limite
    print(j.alterAddPK("DB4P", "Table1_DB4", [0, 1, 2, 3, 4, 5]), end='-')  # Fuera de rango
    print(j.alterAddPK("DB4P", "Table1_DB4", [0, "Colu"]), end="-")  # Error
    print(j.alterAddPK("DB4Pl", "Table1_DB4", [0, 2]), end="-")  # DB no existente
    print(j.alterAddPK("DB4P", "Table1_DB4l", [0, 2]), end="-")  # Tabla no existente
    print(j.alterAddPK("DB4P", "Table1_DB4", [3]), end="-")  # Hay repetidos, error
    # print(j.alterAddPK("DB4P", "Table1_DB4", [0, 2, 3]), end="-")  # Hay repetidos, error
    print(j.alterAddPK("DB4P", "Table1_DB4", [0, 2]), end="-")  # Exitoso
    print(j.alterAddPK("DB4P", "Table1_DB4", [1]))  # ya existe llave primaria

    print("\nProbando el AlterDrop:")
    print(j.alterDropPK("DB4P", 7), end="-")  # Error
    print(j.alterDropPK("DB4Pll", "Table1_DB4"), end="-")  # db no existe
    print(j.alterDropPK("DB4P", "Table1_DB4ll"), end="-")  # tabla no existe
    print(j.alterDropPK("DB4P", "Table2_DB4"), end="-")  # pk no existe
    print(j.alterDropPK("DB4P", "Table1_DB4"))  # Exito

    print("\nProbando el j.alterTable:")
    print(j.alterTable("DB4P", [0], "nuevaTabla"), end="-")  # error
    print(j.alterTable("DB4Pll", "tablaAntigua", "nuevaTabla"), end="-")  # DB no existe
    print(j.alterTable("DB4P", "Table1_DB4ll", "TableNew_DB4"), end="-")  # Tabla no existe
    print(j.alterTable("DB4P", "Table1_DB4", "Table2_DB4"), end="-")  # New existe
    print(j.alterTable("DB4P", "Table1_DB4", "TableNew_DB4"))  # New existe

    print("\nProbando el j.alterAddColumn:")
    print(j.alterAddColumn("DB4P", "TableNew_DB4", "NuevaColumna"), end="-")
    print(j.alterAddColumn("DB4P", "TableNew_DB4", []), end="-")  # error
    print(j.alterAddColumn("DB4Plll", "TableNew_DB4", "NuevaColumna"), end="-")  # db no existe
    print(j.alterAddColumn("DB4P", "TableNew_DB4lll", "NuevaColumna"))  # tabla no existe

    print("\nImpresion 4:")
    testShow("DB4P", 'TableNew_DB4')

    print("\nProbando j.alterDropColumn:")
    print(j.alterDropColumn("DB4P", "TableNew_DB4", [0]), end="-")  # Error
    print(j.alterDropColumn("DB4Pll", "TableNew_DB4", 0), end="-")  # DB no existe
    print(j.alterDropColumn("DB4P", "TableNew_DB4ll", 0), end="-")  # Tabla no existe
    print(j.alterDropColumn("DB4P", "TableNew_DB4", 5), end="-")  # Fuera de limites
    print(j.alterDropColumn("DB4P", "TableNew_DB4", 4), end="-")  # Correcto
    print(j.alterDropColumn("DB4P", "TableNew_DB4", 3), end="-")  # Correcto
    print(j.alterDropColumn("DB4P", "TableNew_DB4", 2), end="-")  # Correcto
    # print(j.alterDropColumn("DB4P", "TableNew_DB4", 1), end="-")  # Correcto
    print(j.alterAddPK("DB4P", "TableNew_DB4", [1]))  # **Prueba de llave primaria. comentar linea superior**
    print(j.alterDropColumn("DB4P", "TableNew_DB4", 1))  # Incorrecto, no se puede vaciar la tabala

    print("\nImpresion 5:")
    testShow("DB4P", 'TableNew_DB4')

    print("\nProbando j.dropTable:")
    print(j.dropTable("DB4P", "TableNew_DB4"))


def testShow(db, tabla):
    print("\nImprimiento DB")
    print(j.showDatabases())
    print("\nImprimiento Tablas", db)
    print(j.showTables(db))
    print("\nImprimiento Tuplas", db)
    print(j.j.extractTable(db, tabla))


# Main()
inicio = default_timer()
test()
fin = default_timer()
print(fin - inicio)