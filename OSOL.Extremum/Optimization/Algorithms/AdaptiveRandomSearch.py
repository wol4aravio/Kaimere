from Optimization.Algorithms.Algorithm import Algorithm
from Numerical_Objects.Vector import Vector

import numpy as np


class AdaptiveRandomSearch(Algorithm):

    @staticmethod
    def generate_random_point_in_sphere(current_point, radius, area):
        normally_distributed = Vector({k: v for k, v in zip(area.keys(), np.random.normal(0.0, 1.0, len(area)))})
        length = np.sqrt(sum(np.array(normally_distributed.values) ** 2))
        shift = (np.random.uniform(0.0, radius) / length) * normally_distributed
        return (current_point + shift).constrain(area)

    def __init__(self, init_radius, factor_small, factor_huge, frequency, max_no_change):
        self._x = None
        self._f_x = None
        self._x_new_1 = None
        self._f_x_new_1 = None
        self._x_new_2 = None
        self._f_x_new_2 = None
        self._radius = None
        self._iteration_id = None
        self._no_change = None
        self._init_radius = init_radius
        self._factor_small = factor_small
        self._factor_huge = factor_huge
        self._frequency = frequency
        self._max_no_change = max_no_change

    @classmethod
    def from_dict(cls, dict_data):
        return cls(dict_data['init_radius'],
                   dict_data['factor_small'],
                   dict_data['factor_huge'],
                   dict_data['frequency'],
                   dict_data['max_no_change'])

    @classmethod
    def from_json(cls, json_data):
        return cls.from_dict(json_data['AdaptiveRandomSearch'])

    def to_dict(self):
        return {
            'init_radius': self._init_radius,
            'factor_small': self._factor_small,
            'factor_huge': self._factor_huge,
            'frequency': self._frequency,
            'max_no_change': self._max_no_change
        }

    def to_json(self):
        return {'AdaptiveRandomSearch': self.to_dict}

    @property
    def current_state(self):
        return {'result': self._x, 'efficiency': self._f_x,
                'radius': self._radius, 'no_change': self._no_change}

    @property
    def iterations(self):
        return [self.generate_new_points, self.modify_radius]

    def initialize(self, f, area, seed):
        self._radius = self._init_radius
        self._iteration_id = 0
        self._no_change = 0
        if seed is None:
            point = {}
            for k, (left, right) in area.items():
                point[k] = np.random.uniform(left, right)
            point = Vector(point)
            self._x = point
            self._f_x = f(point)
        else:
            if isinstance(seed, list):
                self._x = sorted(seed, key=lambda v: f(v))[0]
                self._f_x = f(self._x)
            else:
                self._x = seed
                self._f_x = f(self._x)

    def generate_new_points(self, f, area):
        x = self._x
        radius = self._radius
        factor_small = self._factor_small
        factor_huge = self._factor_huge
        iteration_id = self._iteration_id
        frequency = self._frequency

        self._x_new_1 = AdaptiveRandomSearch.generate_random_point_in_sphere(x, radius, area)
        self._f_x_new_1 = f(self._x_new_1)

        if iteration_id % frequency == 0.0:
            radius_huge = radius * factor_huge
        else:
            radius_huge = radius * factor_small

        self._x_new_2 = AdaptiveRandomSearch.generate_random_point_in_sphere(x, radius_huge, area)
        self._f_x_new_2 = f(self._x_new_2)

        return self.modify_radius

    def modify_radius(self, f, area):
        f_x = self._f_x
        x_new_1 = self._x_new_1
        f_x_new_1 = self._f_x_new_1
        x_new_2 = self._x_new_2
        f_x_new_2 = self._f_x_new_2

        if f_x_new_2 < f_x or f_x_new_1 < f_x:
            if f_x_new_2 < f_x_new_1:
                self._x = x_new_2
                self._f_x = f_x_new_2
                self._radius = self._radius * self._factor_huge
            else:
                self._x = x_new_1
                self._f_x = f_x_new_1
        else:
            self._no_change += 1
            if self._no_change > self._max_no_change:
                self._no_change = 0
                self._radius /= self._factor_small

        self._iteration_id += 1
        return self.generate_new_points
