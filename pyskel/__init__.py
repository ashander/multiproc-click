# pyskel
import time
from random import random

has_legs = False


class Simulation(object):
    def __init__(self, pars):
        self.pars = pars
        self.pd = None


def mod_run(sim_p_tuple):
    sim, p = sim_p_tuple
    _, p2 = sim.pars
    sim.pars = p, p2
    return run(sim)


def run(sim):
    pd = []
    p1, p2 = sim.pars
    for ctr in range(3):
        pd.append([p1, p2])
        time.sleep(random() * 5)

    print(pd)
    return "done"
