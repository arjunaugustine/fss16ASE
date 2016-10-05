#! /usr/bin/python
import random
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
  def __init__(self):
    O.__init__(self)
    self.decisions = []
    self.decisions.append(Decision('x1', 0, 10))
    self.decisions.append(Decision('x2', 0, 10))
    self.decisions.append(Decision('x3', 1, 5))
    self.decisions.append(Decision('x4', 0, 6))
    self.decisions.append(Decision('x5', 1, 5))
    self.decisions.append(Decision('x6', 0, 10))
    self.objectives = [Objective('f1', True), Objective('f2', True)]
    self.points = []

  def evaluate(self, point):
    (x1, x2, x3, x4, x5, x6) = point.decisions
    f1 = -1*(25*((x1-2)**2) + (x2-2)**2 + (x3-1)**2 * (x4-4)**2 + (x5-1)**2)
    f2 = x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2
    point.objectives = [f1, f2]
    point.energy = f1 + f2
    return point.objectives

  @staticmethod
  def is_valid(point):
    """
    Check if point lies in valid range. All points valid in this case.
    :param self:
    :param point:
    :return:
    """
    [x1, x2, x3, x4, x5, x6] = point.decisions
    if x1 + x2 -2 < 0: return False
    if 6 - x1 - x2 < 0: return False
    if 2 - x2 + x1 < 0: return False
    if 2 - x1 + 3*x2 < 0: return False
    if 4 - (x3 - 3)**2 - x4 < 0: return False
    if (x5 - 3)**3 + x6 - 4 < 0: return False
    return True

  def generate_one(self):
    """
    Generate a valid random point, evaluate it and add it to points list.
    :return: generated point
    """
    while True:
      mypoint = Point([random.randint(d.low, d.high) for d in self.decisions])
      if self.is_valid(mypoint):
        self.evaluate(mypoint)
        self.points.append(mypoint)
        return mypoint

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
      if self.is_valid(mypoint):
        self.evaluate(mypoint)
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
      if self.is_valid(mypoint):
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
  def __init__(self, problem):
    O.__init__(self)
    self.Prob = problem()
    self.P = 0.5
    self.MAX_TRIES = 50
    self.MAX_CHANGES = 50
    self.best = self.Prob.generate_one()

  def update_best(self, point):
    if point.energy > self.best.energy:
      say('+')
      self.best = point

  def run(self, problem):
    for i in xrange(self.MAX_TRIES):
      # print 'i =', i,
      say(format(self.best.energy, '4d'))
      solution = problem.generate_one()  # Generate and evaluate a new point.
      say(format(solution.energy, '4d'))
      say('')
      self.update_best(solution)
      for j in xrange(self.MAX_CHANGES):
        # print 'j =', j,
        c = random.choice(problem.decisions)
        # print c
        if self.P < random.random():
          solution = problem.change_decision(solution, c)
          self.update_best(solution)
        else:
          solution = problem.maximize_decision_score(solution, c)
          self.update_best(solution)
      # say()
      print ""
    return self.best


P = Problem()
MWS = MaxWalkSat(Problem)
print MWS.run(P)

