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