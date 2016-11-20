class Node(object):
    def __init__(self, id, name, type, cost=0.0):
        self.id = id
        self.name = name
        self.type = type
        self.parent = None
        self.children = []
        self.cost = cost
        self.present = False

    def getChildren(self):
        return self.children

    def addChild(self, node):
        self.children.append(node)

    def isRoot(self):
        return self.parent == None

    def isLeaf(self):
        return len(self.children)==0

    def __str__(self):
        display = 'ID: ' + self.id + ", Name: " + self.name + ", Type: " + self.type
        if self.parent:
            display += ", Parent: " + self.parent.id
        return display