from queue import PriorityQueue
import numpy as np

TRIALS = 100


def sense_cell(object_map, fail_prob, x, y):
    if object_map.map[x][y] == 1:
        return np.random.binomial(TRIALS, 1 - fail_prob.map[x][y]) / TRIALS
    return np.random.binomial(TRIALS, fail_prob.map[x][y]) / TRIALS


class WeightedGreedy:
    def __init__(self, prob_map, count_map, treshold=5):
        self.prob_map = prob_map
        self.count_map = count_map
        self.treshold = treshold
        self.queue = PriorityQueue()

        for i in range(prob_map.size):
            for j in range(prob_map.size):
                self.queue.put([-prob_map.map[i][j], [i, j]])

    def iterate(self, object_map, fail_prob):
        step = -1
        while not self.queue.empty():
            step += 1
            priority, point = self.queue.get_nowait()
            print('Step {1}: {0}'.format(str(point), step))
            new_prob = sense_cell(object_map, fail_prob, point[0], point[1])
            if new_prob > .5:
                count = self.count_map.map[point[0]][point[1]] + 1
                if count == self.treshold:
                    return point
                self.count_map.map[point[0]][point[1]] = count
            self.queue.put([-new_prob, point])
