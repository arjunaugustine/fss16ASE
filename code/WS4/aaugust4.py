#! /usr/bin/python

# %matplotlib inline
# All the imports
from __future__ import print_function, division
import pom3_ga, sys
import pickle
# import

# TODO 1: Enter your unity ID here
__author__ = "aaugust4"

# TODO 2: To compute most measures, data(i.e objectives) is normalized.
# TODO 2: Normalization is scaling the data between 0 and 1. Why do we normalize?
"""
Answer: Each objective has to be brought down to one simple scale so that each of them is comparable.
"""


def normalize(problem, points):
  """
  Normalize all the objectives
  in each point and return them
  """
  meta = problem.objectives
  all_objs = []
  for point in points:
    objs = []
    for i, o in enumerate(problem.evaluate(point)):
      low, high = meta[i].low, meta[i].high
      # TODO 3: Normalize 'o' between 'low' and 'high'; Then add the normalized value to 'objs'
      if high == low: objs.append(0); continue;
      objs.append((o - low)/(high - low))
    all_objs.append(objs)
  return all_objs

"""
Data Format
For our experiments we store the data in the following format.
data = {
            "expt1":[repeat1, repeat2, ...],
            "expt2":[repeat1, repeat2, ...],
            .
            .
            .
       }
repeatx = [objs1, objs2, ....]     // All of the final population
objs1 = [norm_obj1, norm_obj2, ...] // Normalized objectives of each member of the final population.
"""


"""
Performing experiments for [5, 10, 50] generations.
"""
problem = pom3_ga.POM3()
pop_size = 10
repeats = 10
test_gens = [5, 10, 50]


def save_data(file_name, data):
  """
  Save 'data' to 'file_name.pkl'
  """
  with open(file_name + ".pkl", 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


def load_data(file_name):
  """
  Retrieve data from 'file_name.pkl'
  """
  with open(file_name + ".pkl", 'rb') as f:
    return pickle.load(f)


def build(problem, pop_size, repeats, test_gens):
  """
  Repeat the experiment for 'repeats' number of repeats for each value in 'test_gens'
  """
  tests = {t: [] for t in test_gens}
  tests[0] = []  # For Initial Population
  for _ in range(repeats):
    init_population = pom3_ga.populate(problem, pop_size)
    pom3_ga.say(".")
    for gens in test_gens:
      tests[gens].append(normalize(problem, pom3_ga.ga(problem, init_population, retain_size=pop_size, gens=gens)[1]))
    tests[0].append(normalize(problem, init_population))
  print("\nCompleted")
  return tests


"""
Repeat Experiments
"""
# tests = build(problem, pop_size, repeats, test_gens)

"""
Save Experiment Data into a file
"""
# save_data("dump", tests)

"""
Load the experimented data from dump.
"""
tests = load_data("dump")

"""
Reference Set
Almost all the traditional measures you consider need a reference set for its computation.
A theoritical reference set would be the ideal pareto frontier. This is fine for
  a) Mathematical Models: Where we can solve the problem to obtain the set.
  b) Low Runtime Models: Where we can do a one time exaustive run to obtain the model.
But most real world problems are neither mathematical nor have a low runtime.
So what do we do?. Compute an approximate reference set
One possible way of constructing it is:
  1. Take the final generation of all the treatments.
  2. Select the best set of solutions from all the final generations
"""

def make_reference(problem, *fronts):
  """
  Make a reference set comparing all the fronts.
  Here the comparison we use is bdom. It can
  be altered to use cdom as well
  """
  retain_size = len(fronts[0])
  reference = []
  for front in fronts:
    reference += front

  def bdom(one, two):
    """
    Return True if 'one' dominates 'two'
    else return False
    :param one - [pt1_obj1, pt1_obj2, pt1_obj3, pt1_obj4]
    :param two - [pt2_obj1, pt2_obj2, pt2_obj3, pt2_obj4]
    """
    dominates = False
    for i, obj in enumerate(problem.objectives):
      gt, lt = pom3_ga.gt, pom3_ga.lt
      better = lt if obj.do_minimize else gt
      # TODO 4: Use the varaibles declared above to check if one dominates two
      if better(one[i], two[i]):
        dominates = True
      elif one[i] != two[i]:
        return False
    return dominates

  def fitness(one, dom):
    return len([1 for another in reference if dom(one, another)])

  fitnesses = []
  for point in reference:
    fitnesses.append((fitness(point, bdom), point))
  reference = [tup[1] for tup in sorted(fitnesses, reverse=True)]
  return reference[:retain_size]


make_reference(problem, tests[5][0], tests[10][0], tests[50][0])

"""
Calculating Spread:
Ideal delta is zero. All points that we obtained on the pareto frontier should be equally spaced,
and their extremes should be the extreme possible solutions. d_f and d_l are distances of the extreme
obtained solutions to the extreme possible solutions. d_i is the distance between two adjascent solutions
and d_bar is the average such distance. So, the numerator of delta is a function of all these values.
"""

def eucledian(one, two):
  """
  Compute Eucledian Distance between
  2 vectors. We assume the input vectors
  are normalized.
  :param one: Vector 1
  :param two: Vector 2
  :return:
  """
  # TODO 5: Code up the eucledian distance. https://en.wikipedia.org/wiki/Euclidean_distance
  dist = (sum([(o - t)**2 for o,t in zip(one,two)]) / len(one))**0.5
  return dist

def sort_solutions(solutions):
  """
  Sort a list of list before computing spread
  """
  def sorter(lst):
    m = len(lst)
    weights = reversed([10 ** i for i in xrange(m)])
    return sum([element * weight for element, weight in zip(lst, weights)])
  return sorted(solutions, key=sorter)


def closest(one, many):
  min_dist = sys.maxint
  closest_point = None
  for this in many:
    dist = eucledian(this, one)
    if dist < min_dist:
      min_dist = dist
      closest_point = this
  return min_dist, closest_point

def spread(obtained, ideals):
  """
  Calculate the spread (a.k.a diversity)
  for a set of solutions
  """
  s_obtained = sort_solutions(obtained)
  s_ideals = sort_solutions(ideals)
  d_f = closest(s_ideals[0], s_obtained)[0]
  d_l = closest(s_ideals[-1], s_obtained)[0]
  n = len(s_ideals)
  distances = []
  for i in range(len(s_obtained)-1):
    distances.append(eucledian(s_obtained[i], s_obtained[i+1]))
  d_bar = sum(distances)/len(distances)
  # TODO 6: Compute the value of spread using the definition defined in the previous cell.
  d_sum = sum([abs(d_i - d_bar) for d_i in distances])
  delta = (d_f + d_l + d_sum) / (d_f + d_l + (n-1) * d_bar)
  return delta


ref = make_reference(problem, tests[5][0], tests[10][0], tests[50][0])

print(spread(tests[5][0], ref))
print(spread(tests[10][0], ref))
print(spread(tests[50][0], ref))

"""
IGD = inter-generational distance; i.e. how good are you compared to the best known?
Find a reference set (the best possible solutions)
For each optimizer
- For each item in its final Pareto frontier
- Find the nearest item in the reference set and compute the distance to it.
- Take the mean of all the distances. This is IGD for the optimizer
Note that the less the mean IGD,
the better the optimizer since this means its solutions are closest to the best of the best.
"""

def igd(obtained, ideals):
  """
  Compute the IGD for a
  set of solutions
  :param obtained: Obtained pareto front
  :param ideals: Ideal pareto front
  :return:
  """
  # TODO 6: Compute the value of IGD using the definition defined in the previous cell.
  igd_val = sum([closest(ideal, obtained)[0] for ideal in ideals]) / len(ideals)
  return igd_val

ref = make_reference(problem, tests[5][0], tests[10][0], tests[50][0])

print(igd(tests[5][0], ref))
print(igd(tests[10][0], ref))
print(igd(tests[50][0], ref))

import sk

sk = reload(sk)


def format_for_sk(problem, data, measure):
  """
  Convert the experiment data into the format
  required for sk.py and computet the desired
  'measure' for all the data.
  """
  gens = data.keys()
  reps = len(data[gens[0]])
  measured = {gen: ["gens_%d" % gen] for gen in gens}
  for i in range(reps):
    ref_args = [data[gen][i] for gen in gens]
    ref = make_reference(problem, *ref_args)
    for gen in gens:
      measured[gen].append(measure(data[gen][i], ref))
  return measured


def report(problem, tests, measure):
  measured = format_for_sk(problem, tests, measure).values()
  sk.rdivDemo(measured)


print("*** IGD ***")
report(problem, tests, igd)
print("\n*** Spread ***")
report(problem, tests, spread)