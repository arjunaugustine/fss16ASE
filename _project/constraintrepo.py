class ConstraintRepo(object):
  def __init__(self):
    self.constraints = []
    self.flags = {}

  def addConstraint(self, constraint):
    for flag in constraint.flags:
      self.flags.setdefault(flag.id, []).append(flag)
    self.constraints.append(constraint)

  def getNumOfConstraintsViolated(self):
    count = 0
    for constraint in self.constraints:
      if constraint.isViolated():
        count += 1
    return count

  def setFlag(self, id):
    if id not in self.flags: return
    for flag in self.flags[id]:
      flag.setFlag()
