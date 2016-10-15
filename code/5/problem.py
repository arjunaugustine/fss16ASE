#! /usr/bin/python
import random, sys
import copy, math, sys

def shuffle(lst):
    """
    Shuffle a list
    """
    random.shuffle(lst)
    return lst


def say(lst):
  """
  Print whithout going to new line
  """
  print lst,
  sys.stdout.flush()


class O:
    """
    Basic Class which
        - Helps dynamic updates
        - Pretty Prints
    """

    def __init__(self, **kwargs):
        self.has().update(**kwargs)

    def has(self):
        return self.__dict__

    def update(self, **kwargs):
        self.has().update(kwargs)
        return self

    def __repr__(self):
        show = [':%s %s' % (k, self.has()[k])
                for k in sorted(self.has().keys())
                if k[0] is not "_"]
        txt = ' '.join(show)
        if len(txt) > 60:
            show = map(lambda x: '\t' + x + '\n', show)
        return '{' + ' '.join(show) + '}'


class Decision(O):
  """
  Class indicating decision of a problem
  """
  def __init__(self, name, low, high):
    """
    :param name: Name of decision
    :param low: Least value of decision
    :param high: Maximum value of decision
    """
    O.__init__(self, name=name, low=low, high=high)


class Objective(O):
  """
  Class indicating objective of a problem
  """
  def __init__(self, name, domin=True):
    """
    :param name: Name of decision
    :param domin: Want to minimize? or Maximize?
    """
    O.__init__(self, name=name, domin=domin)


class Point(O):
  """
  Class indicating a member of population
  """
  def __init__(self, decisions):
    O.__init__(self)
    self.decisions = decisions
    self.objectives = None
    self.energy = None

  def __eq__(self, other):
    return self.decisions == other.decisions

  def clone(self):
    new = Point(self.decisions)
    new.objectives = self.objectives
    new.energy = self.energy
    return new


class Problem(O):
  """
  Class representing the Osyczka2 problem
  """

  def __init__(self, decisions, objectives):
    """
    Initialize Problem.
    :param decisions -  Metadata for Decisions
    :param objectives - Metadata for Objectives
    """
    O.__init__(self)
    self.decisions = decisions
    self.objectives = objectives

  @staticmethod
  def evaluate(point):
    assert False # Problem should not be instantiated separately. The parent evaluate method would override this.
    return point.objectives

  @staticmethod
  def is_valid(self, point):
    """
    Checks whether the decisions lie in the low to high limits.
    :param self:
    :param point:
    :return:
    """
    print " BLOODDDDYY HEELLLL FUUUCKCKKKKERRRR"
    # print self
    # print point
    for i,d in enumerate(point.decisions):
      if d < self.decisions[i].low or d > self.decisions[i].high:
        return False
    return True

  def generate_one(self, retries=500):
    """
    Generate a valid random point, evaluate it and add it to points list.
    :return: generated point
    """
    # print self
    for _ in xrange(retries):
      point = Point([random.randint(d.low, d.high) for d in self.decisions])
      # print "", "", point
      if self.is_valid(self, point):
        self.evaluate(self, point)
        self.points.append(point)
        return point
    print "Fuck this"
    # sys.exit()
    raise RuntimeError("Exceeded max runtimes of %d" % retries)


class Osyczka2(Problem):

  def __init__(self):
    """
    Initialize the POM3 classes
    The model has 4 objectives
    Cost in [0,10000] - Minimize
    Score in [0,1] - Maximize
    Completion in [0,1] - Maximize
    Idle in [0,1] - Minimize
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
  def evaluate(self, point):
    (x1, x2, x3, x4, x5, x6) = point.decisions
    f1 = -1*(25*((x1-2)**2) + (x2-2)**2 + (x3-1)**2 * (x4-4)**2 + (x5-1)**2)
    f2 = x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2
    point.objectives = [f1, f2]
    point.energy = f1 + f2
    return point.objectives

  @staticmethod
  def is_valid(self, point):
    """
    Check if point lies in valid range. All points valid in this case.
    :param self:
    :param point:
    :return:
    """
    [x1, x2, x3, x4, x5, x6] = point.decisions
    if x1 + x2 -2 < 0:
      # print '1'
      return False
    if 6 - x1 - x2 < 0:
      # print '2'
      return False
    if 2 - x2 + x1 < 0:
      # print '3'
      return False
    if 2 - x1 + 3*x2 < 0:
      # print '4'
      return False
    if 4 - (x3 - 3)**2 - x4 < 0:
      # print '5'
      return False
    if (x5 - 3)**3 + x6 - 4 < 0:
      # print '6'
      return False
    for i, d in enumerate(point.decisions):
      if d < self.decisions[i].low or d > self.decisions[i].high:
        print i, d, self.decisions[i].low, self.decisions[i].high
        return False
    return True
    # return Problem.is_valid(Problem, point)

  def change_decision(self, point, c):
    """
    Change a random decision in the point and return a valid point
    :param point:
    :param c: decision
    :return:
    """
    mypoint = point.clone()
    while True:
      mypoint.decisions = point.decisions
      mypoint.decisions[int(c.name[1])-1] = random.randint(c.low, c.high)
      if self.is_valid(self, mypoint):
        self.evaluate(self, mypoint)
        self.points.append(mypoint)
        say('!')
      else:
        say('.')
      return mypoint

  def maximize_decision_score(self, point, c):
    """
    Change decision c in point that maximizes score for point
    :param point:
    :param c:
    :return:
    """
    mypoint = point.clone()
    bestpoint = point
    id = int(c.name[1])-1
    for val in xrange(int(math.ceil(c.low)), int(math.floor(c.high))):
      mypoint.decisions[id] = val
      if self.is_valid(self, mypoint):
        if mypoint.energy > bestpoint.energy:
          bestpoint = mypoint
    print_char = ',' if bestpoint.energy is point.energy else '|'
    say(print_char)
    return bestpoint


class MaxWalkSat(O):
  """
  FOR i = 1 to max-tries DO
  solution = random assignment
  FOR j =1 to max-changes DO
    IF  score(solution) > threshold
        THEN  RETURN solution
    FI
    c = random part of solution
    IF    p < random()
    THEN  change a random setting in c
    ELSE  change setting in c that maximizes score(solution)
    FI
  RETURN failure, best solution found
  """
  def __init__(self, model):
    O.__init__(self)
    self.Model = model()
    self.P = 0.5
    self.MAX_TRIES = 25
    self.MAX_CHANGES = 25
    self.best = self.Model.generate_one()

  def update_best(self, point):
    if point.energy > self.best.energy:
      say('+')
      self.best = point

  def run(self, model):
    for i in xrange(self.MAX_TRIES):
      say(format(self.best.energy, '4d'))
      solution = model.generate_one()  # Generate and evaluate a new point.
      say(format(solution.energy, '4d'))
      say('')
      self.update_best(solution)
      for j in xrange(self.MAX_CHANGES):
        c = random.choice(model.decisions)
        if self.P < random.random():
          solution = model.change_decision(solution, c)
          self.update_best(solution)
        else:
          solution = model.maximize_decision_score(solution, c)
          self.update_best(solution)
      print ""
    return self.best


P = Osyczka2()
MWS = MaxWalkSat(Osyczka2)
print MWS.run(P)
print ""
