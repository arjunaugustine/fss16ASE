class Node(object):
  def __init__(self, id, name, type):
    self.id = id
    self.name = name
    self.type = type
    self.parent = None
    self.children = []

  def getChildren(self):
    return self.children

  def addChild(self, node):
    self.children.append(node)

  def isRoot(self):
    return self.parent == None

  def isLeaf(self):
    return len(self.children)

  def __str__(self):
    display = 'ID: ' + self.id + ", Name: " + self.name + ", Type: " + self.type
    if self.parent:
      display += ", Parent: " + self.parent.id
    return display