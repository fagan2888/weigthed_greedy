from queue import PriorityQueue
import numpy as np
import turtle

TRIALS = 100


def sense_cell(object_map, fail_prob, x, y):
    if object_map.map[x][y] == 1:
        return np.random.binomial(TRIALS, 1 - fail_prob.map[x][y]) / TRIALS
    return np.random.binomial(TRIALS, fail_prob.map[x][y]) / TRIALS


def euclidean(A, B):
    return ((A[0]-B[0])**2+(A[1]-B[1])**2)**0.5


class WeightedGreedy:
    def __init__(self, prob_map, count_map, treshold=5):
        self.prob_map = prob_map
        self.count_map = count_map
        self.treshold = treshold
        self.queue = PriorityQueue()

        for i in range(prob_map.size):
            for j in range(prob_map.size):
                self.queue.put([-prob_map.map[i][j], [i, j]])

    def iterate(self, object_map, fail_prob, coloring=False, print=False):
        step = -1
        lastpoint = [0, 0]
        flight = 0
        if coloring: 
            turtle.Turtle
            turtle.clear()
            turtle.color('red', 'yellow')
            turtle.penup()
            for each in object_map.get_index_of_object():
                turtle.goto((each[0]*60-300,each[1]*60-300))
                turtle.pendown()
                turtle.dot()
                turtle.penup()
            turtle.goto((lastpoint[0]*60-300, lastpoint[1]*60-300))
            turtle.pendown()

        while not self.queue.empty():
            step += 1
            priority, point = self.queue.get_nowait()

            if coloring:
                turtle.goto((point[0]*60-300, point[1]*60-300))

            flight += euclidean(lastpoint, point)
            lastpoint = point
            new_prob = sense_cell(object_map, fail_prob, point[0], point[1])
            if print:
                print('Step {1}: {0}, {2}, {3}'.format(str(point), step, priority, new_prob))
            if new_prob > .5:
                count = self.count_map.map[point[0]][point[1]] + 1
                if count == self.treshold:
                    if print: print('Steps:{0}, Total distance:{1}'.format(step, flight))
                    if point in object_map.get_index_of_object():
                        if print:
                            print('Success')
                        succ = 1
                    break
                self.count_map.map[point[0]][point[1]] = count
            self.queue.put([-new_prob, point])

        if coloring:
            turtle.end_fill()
            turtle.done()

        return step, flight, succ
            
    def iterate_distance(self, object_map, fail_prob, coloring=False, print=True):
        step = -1
        lastpoint = [0, 0]
        flight = 0
        if coloring: 
            turtle.Turtle
            turtle.clear()
            turtle.color('red', 'yellow')
            turtle.penup()
            for each in object_map.get_index_of_object():
                turtle.goto((each[0]*60-300,each[1]*60-300))
                turtle.pendown()
                turtle.dot()
                turtle.penup()
            turtle.goto((lastpoint[0]*60-300,lastpoint[1]*60-300))
            turtle.pendown()
        while True:
            step += 1
            self.queue = PriorityQueue()
            for i in range(self.prob_map.size):
                for j in range(self.prob_map.size):
                    nprob=-self.prob_map.map[i][j]+euclidean(lastpoint, [i,j])/((2*(self.prob_map.size**2))**0.5)
                    self.queue.put([nprob, [i, j]])
            
            priority, point = self.queue.get_nowait()
            if coloring: turtle.goto((point[0]*60-300,point[1]*60-300))
            flight+=euclidean(lastpoint, point)
            lastpoint=point
            new_prob = sense_cell(object_map, fail_prob, point[0], point[1])
            self.prob_map.map[point[0]][point[1]]=new_prob
            if print: print('Step {1}: {0}, {2}, {3}'.format(str(point), step, priority, new_prob))
            if new_prob > .5:
                count = self.count_map.map[point[0]][point[1]] + 1
                if count == self.treshold:
                    if print: print('Steps:{0}, Total distance:{1}'.format(step, flight))
                    succ=0
                    if point in object_map.get_index_of_object(): 
                        if print: print('Success')
                        succ=1
                    break
                self.count_map.map[point[0]][point[1]] = count

        if coloring: turtle.end_fill()
        if coloring: turtle.done()
        return step, flight, succ
            
            
            

