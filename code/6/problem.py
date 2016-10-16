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
  def eval(point):
    assert False, 'Problem should not be instantiated separately. ' \
                  'The parent evaluate method would override this.'
    return point.objectives

  @staticmethod
  def ok(self, point):
    """
    :param self:
    :param point:
    :return:
    """
    assert False, 'Problem should not be instantiated separately. ' \
                  'The parent ok method would override this.'
    return True

  def any(self, retries=500):
    """
    Generate a valid random point, evaluate it and add it to points list.
    :return: generated point
    """
    for _ in xrange(retries):
      point = Point([random.randint(int(d.low), d.high) for d in self.decisions])
      if self.ok(self, point):
        self.eval(self, point)
        self.points.append(point)
        return point
    raise RuntimeError("Exceeded max runtimes of %d" % retries)

