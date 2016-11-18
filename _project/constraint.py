class Constraint(object):
  def __init__(self):
    self.flags = []

  def addFlag(self, flag):
    self.flags.append(flag)

  def isViolated(self):
    for flag in self.flags:
      if flag.getFlag(): return False
    return True
