from models import *

epsilon = 0.001

def sa(model, kmax=1000, emax=625):
  """
  s := s0; e := E(s)                  // Initial state, energy.
  sb := s; eb := e                    // Initial "best" solution
  k := 0                              // Energy evaluation count.
  WHILE k < kmax and e > emax         // While time remains & not good enough:
    sn := neighbor(s)                 //   Pick some neighbor.
    en := E(sn)                       //   Compute its energy.
    IF    en < eb                     //   Is this a new best?
    THEN  sb := sn; eb := en          //     Yes, save it.
          print "!"
    FI
    IF    en < e                      // Should we jump to better?
    THEN  s := sn; e := en            //    Yes!
          print "+"
    FI
    ELSE IF P(e, en, k/kmax) < rand() // Should we jump to worse?
    THEN  s := sn; e := en            //    Yes, change state.
          print "?"
    FI
    print "."
    k := k + 1                        //   One more evaluation done
    if k % 50 == 0: print "\n",sb
  RETURN sb                           // Return the best solution found.
  :param model:
  :param kmax:
  :return:
  """

  def set_baseline(n_times=200):
    """
    sets the baseline minimum energy and maximum energy
    :param n_times: int Number of samples to consider to set baseline values
    :return: None
    """
    rand_point = model.any()
    max_e = rand_point.energy
    for _ in xrange(n_times):
      rand_point = model.any()
      if rand_point.energy > max_e: max_e = rand_point.energy
    return max_e

  def get_neighbor(point, retries=50):
    """
    Select a random decision and choose another value for it in valid range.
    Keep iterating until you have a valid neighbor and return this.
    :param point:
    :return:
    """
    p = point.clone()
    while retries:
      decision = random.randint(0, len(p.decisions)-1)
      p.decisions[decision] = random.randint(int(model.decisions[decision].low),
                                             int(model.decisions[decision].high))
      if model.ok(model, p):
        model.eval(model, p)
        model.points.append(p)
        return p
      else:
        p.decisions = point.decisions
        retries -= 1
    return point

  def prob(e, en, t, emax):
    """
    probability function
    :param e: current energy
    :param en: new energy
    :param t: temperature
    :return:e^ ((e-en)/t)
    """
    global epsilon
    if t is 0:
      t = epsilon
    var = float(en - e) / math.fabs(emax) / t
    # print e, en, emax
    # print 'var:', var
    return math.exp(var)

  s = model.any()
  sb = s
  k = 0
  emax = set_baseline()
  while k < kmax and sb.energy < emax:
    sn = get_neighbor(s)
    if not k % 25:
      print ""
      print format(sb.energy, '12d'), ' ',
      print format(sn.energy, '12d'), ' ',
    if sn.energy > sb.energy:
      sb = sn
      say('!')
    if sn.energy > s.energy:
      s = sn
      say('+')
    elif prob(s.energy, sn.energy, k/kmax, emax) < random.random():
      s = sn
      say('?')
    else:
      say('.')
    k += 1
  print ""
  return sb


def mws(model, max_tries=25, max_changes=25, p=0.5):
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
  best = model.any()

  def update_best(point, best):
    if point.energy > best.energy:
      say('+')
      return point
    return best

  def change_decision(point, c):
    """
    Change a random decision in the point and return a valid point
    :param point:
    :param c: decision
    :return:
    """

    mypoint = point.clone()
    while True:
      mypoint.decisions = point.decisions
      mypoint.decisions[int(c.name[1]) - 1] = random.randint(int(c.low), int(c.high))
      if model.ok(model, mypoint):
        model.eval(model, mypoint)
        model.points.append(mypoint)
        say('!')
      else:
        say('.')
      return mypoint

  def maximize_decision_score(point, c):
    """
    Change decision c in point that maximizes score for point
    :param point:
    :param c:
    :return:
    """
    mypoint = point.clone()
    bestpoint = point
    id = int(c.name[1]) - 1
    for val in xrange(int(math.ceil(c.low)), int(math.floor(c.high))):
      mypoint.decisions[id] = val
      if model.ok(model, mypoint):
        if mypoint.energy > bestpoint.energy:
          bestpoint = mypoint
    print_char = ',' if bestpoint.energy is point.energy else '|'
    say(print_char)
    return bestpoint

  for i in xrange(max_tries):
    say(format(best.energy, '12d'))
    solution = model.any()  # Generate and evaluate a new point.
    say(format(solution.energy, '12d'))
    say('')
    best = update_best(solution, best)
    for j in xrange(max_changes):
      c = random.choice(model.decisions)
      if p < random.random():
        solution = change_decision(solution, c)
        best = update_best(solution, best)
      else:
        solution = maximize_decision_score(solution, c)
        best = update_best(solution, best)
    print ""
  return best

for model in [Schaffer, Osyczka2, Kursawe]:
  for optimizer in [sa, mws]:
    print ""
    sys.stdout.flush()
    print(optimizer, model)
    print(optimizer(model()))
