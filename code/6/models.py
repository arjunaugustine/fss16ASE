from problem import *


class Osyczka2(Problem):

  def __init__(self):
    """
    Initialize the Osyczka2 class
    """
    self.points = []
    names = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    lows = [0, 0, 1, 0, 1, 0]
    highs = [10, 10, 5, 6, 5, 10]
    # TODO 2: Use names, lows and highs defined above to code up decision
    # and objective metadata for POM3.
    decisions = [Decision(n, l, h) for n, l, h in zip(names, lows, highs)]
    objectives = [Objective("f1", True), Objective("f2", True)]
    Problem.__init__(self, decisions, objectives)

  @staticmethod
  def eval(self, point):
    (x1, x2, x3, x4, x5, x6) = point.decisions
    f1 = -1*(25*((x1-2)**2) + (x2-2)**2 + (x3-1)**2 * (x4-4)**2 + (x5-1)**2)
    f2 = x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2
    point.objectives = [f1, f2]

    def minimize(i):
      return -1 if self.objectives[i].domin else 1

    point.energy = int(f1 * minimize(0) + f2 * minimize(1))
    return point.objectives

  @staticmethod
  def ok(self, point):
    """
    Check if point lies in valid range. All points valid in this case.
    :param self:
    :param point:
    :return:
    """
    [x1, x2, x3, x4, x5, x6] = point.decisions
    if x1 + x2 -2 < 0:
      return False
    if 6 - x1 - x2 < 0:
      return False
    if 2 - x2 + x1 < 0:
      return False
    if 2 - x1 + 3*x2 < 0:
      return False
    if 4 - (x3 - 3)**2 - x4 < 0:
      return False
    if (x5 - 3)**3 + x6 - 4 < 0:
      return False
    for i, d in enumerate(point.decisions):
      if d < self.decisions[i].low or d > self.decisions[i].high:
        print i, d, self.decisions[i].low, self.decisions[i].high
        return False
    return True


class Kursawe(Problem):

  def __init__(self):
    """
    Initialize the Kursawe class
    """
    self.points = []
    names = ['x1', 'x2', 'x3']
    lows = [-5, -5, -5]
    highs = [5, 5, 5]
    # TODO 2: Use names, lows and highs defined above to code up decision
    # and objective metadata for POM3.
    decisions = [Decision(n, l, h) for n, l, h in zip(names, lows, highs)]
    objectives = [Objective("f1", True), Objective("f2", True)]
    Problem.__init__(self, decisions, objectives)

  @staticmethod
  def eval(self, point):
    (x1, x2, x3) = point.decisions
    f1, f2 = 0, 0
    f1 = -10*math.e**(-0.2*math.sqrt(x1**2 + x2**2)) \
         -10*math.e**(-0.2*math.sqrt(x2**2 + x3**2))
    for x in point.decisions:
      f2 += (math.fabs(x)**0.8 + 5*math.sin(x**3))
    point.objectives = [f1, f2]

    def minimize(i):
      return -1 if self.objectives[i].domin else 1

    point.energy = int(f1*minimize(0) + f2*minimize(1))
    return point.objectives

  @staticmethod
  def ok(self, point):
    """
    Check if point lies in valid range. All points valid in this case.
    :param self:
    :param point:
    :return:
    """
    return True


class Schaffer(Problem):

  def __init__(self):
    """
    Initialize the Schaffer class
    """
    self.points = []
    names = ['x1']
    lows = [10**-5]
    highs = [10**5]
    # TODO 2: Use names, lows and highs defined above to code up decision
    # and objective metadata for POM3.
    decisions = [Decision(n, l, h) for n, l, h in zip(names, lows, highs)]
    objectives = [Objective("f1", True), Objective("f2", True)]
    Problem.__init__(self, decisions, objectives)

  @staticmethod
  def eval(self, point):
    f1 = point.decisions[0]**2
    f2 = (point.decisions[0]-2)**2
    point.objectives = [f1, f2]

    def minimize(i):
      return -1 if self.objectives[i].domin else 1

    point.energy = int(f1*minimize(0) + f2*minimize(1))
    return point.objectives

  @staticmethod
  def ok(self, point):
    """
    Check if point lies in valid range. All points valid in this case.
    :param self:
    :param point:
    :return:
    """
    return True
