import numpy as np


class Map:
    def __init__(self, size):
        self.size = size
        self.map = np.array([[1] * size] * size)


class FailProbMap(Map):
    # Map that has the probabilities
    def __init__(self, size, min_failure=.10, max_failure=.4):
        super().__init__(size)
        self.map = self.map * np.random.randint(int(min_failure*1e6), int(max_failure*1e6), [self.size, self.size]) / 1e6


class ObjectMap(Map):
    # Map that has x amount of objects
    def __init__(self, size, objects=1):
        super().__init__(size)
        self.map = np.array([[0] * self.size] * self.size)
        coord = np.random.randint(0, self.size * self.size - 1, objects)
        coord = [[int(each / self.size), int(each % self.size)] for each in coord]
        for each in coord:
            self.map[each[0], each[1]] = 1

    def get_index_of_object(self):
        result = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.map[i][j] == 1:
                    result.append([i, j])

        return result


class ProbMap(Map):
    def __init__(self, size):
        super().__init__(size)
        self.map = np.array([[0] * size] * size)

    def generate_prob_from_map(self, object_map):
        self.generate_prob_random()
        ones = object_map.get_index_of_object()
        for one in ones:
            self.map[one[0]][one[1]] = np.random.randint(5000, 9999) / 10000
            if one[0]+1 < self.size:
                if one[1]+1 < self.size:
                    self.map[one[0] + 1][one[1] + 1] = np.random.randint(5000, 9999) / 10000
                if one[1]-1 >= 0:
                    self.map[one[0] + 1][one[1] -1] = np.random.randint(5000, 9999) / 10000

                self.map[one[0] + 1][one[1]] = np.random.randint(5000, 9999) / 10000

            if one[0] -1 < self.size:
                self.map[one[0] - 1][one[1]] = np.random.randint(5000, 9999) / 10000
                if one[1]-1 >= 0:
                    self.map[one[0] - 1][one[1] - 1] = np.random.randint(5000, 9999) / 10000
                if one[1]-1 < self.size:
                    self.map[one[0] - 1][one[1] - 1] = np.random.randint(5000, 9999) / 10000
            if one[1] + 1 < self.size:
                self.map[one[0]][one[1] + 1] = np.random.randint(5000, 9999) / 10000
            if one[1] -1 >= 0:
                self.map[one[0]][one[1] - 1] = np.random.randint(5000, 9999) / 10000

    def generate_prob_random(self):
        self.map = np.array([[1] * self.size] * self.size)
        self.map = self.map * np.random.randint(1, 9999, [self.size, self.size]) / 10000


class CountMap(Map):
    def __init__(self, size):
        super().__init__(size)
        self.size = size
        self.map = np.array([[0] * size] * size)
