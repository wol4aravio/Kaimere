from abc import ABC, abstractmethod
from contracts import contract, new_contract, ContractsMeta
import sys

from osol.extremum.optimization.basic.vector import Vector
from osol.extremum.optimization.basic.terminator import Terminator, TerminatorExceptions


new_contract("terminator", Terminator)
new_contract("vector", Vector)


class Algorithm(ABC, metaclass=ContractsMeta):
    """ Abstract class that describes desired interface for optimization algorithm """

    @abstractmethod
    @contract
    def initialize(self, f, search_area, seed_state):
        """ Procedure that initializes optimization algorithm

            :param f: objective function
            :type f: terminator

            :param search_area: search area
            :type search_area: dict(str:tuple(number, number))

            :param seed_state: seed state for the algorithm
            :type seed_state: dict(str:*)|None

            :returns: current state of the algorithm
            :rtype: dict(str:*)
        """

    @abstractmethod
    @contract
    def main_cycle(self, f, search_area, **kwargs):
        """ Main cycle of the algorithm

            :param f: objective function
            :type f: terminator

            :param search_area: search area
            :type search_area: dict(str:tuple(number, number))

            :param kwargs: current state of the algorithm
            :type kwargs: dict(str:*)

            :returns: current state of the algorithm
            :rtype: dict(str:*)
        """

    @abstractmethod
    @contract
    def terminate(self, f, search_area, **kwargs):
        """ Termination part of the algorithm

            :param f: objective function
            :type f: terminator

            :param search_area: search area
            :type search_area: dict(str:tuple(number, number))

            :param kwargs: current state of the algorithm
            :type kwargs: dict(str:*)

            :returns: solution
            :rtype: vector
        """

    @contract
    def optimize(self, f, search_area, seed_state=None, max_iter=None):
        """ Optimization procedure

            :param f: objective function
            :type f: terminator

            :param search_area: search area
            :type search_area: dict(str:tuple(number, number))

            :param seed_state: seed state for the algorithm
            :type seed_state: dict(str:*)|None

            :param max_iter: maximum allowed number of iterations
            :type max_iter: int|None

            :returns: solution
            :rtype: vector
        """
        current_state = self.initialize(f, search_area, seed_state)
        try:
            for _ in range(max_iter or sys.maxsize):
                current_state = self.main_cycle(f, search_area, **current_state)
        except TerminatorExceptions.StopWorkException:
            pass
        return self.terminate(f, search_area, **current_state)
