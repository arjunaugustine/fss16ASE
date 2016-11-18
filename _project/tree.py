class Tree(object):
  def __init__(self):
    self.root = None

  def getRoot(self):
    return self.root

  def addNode(self, node):
    if node.type == 'r':
      self.root = node
    else:
      self.addNodeToTree(self.root, node)

  def addNodeToTree(self, root, node):
    for child in root.getChildren():
      if child.id in node.id:
        self.addNodeToTree(child, node)
        return
    root.addChild(node)
    node.parent = root

  def visualize(self):
    self.visualizeTree(self.root)

  def visualizeTree(self, root):
    print root
    for child in root.getChildren():
      self.visualizeTree(child)

