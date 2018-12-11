import numpy as np

from .Map import ObjectMap, FailProbMap, ProbMap, CountMap
from .WeightedGreedy import WeightedGreedy

np.random.seed(10)
SIZE = 10
NUM_OBJECTS = 1


def main():
    # Inicializar Mapas de: probabilidad de falla (15-40%), ubicacion, mapa probabilidades, countMap
    fail_prob = FailProbMap(SIZE)
    object_map = ObjectMap(SIZE, NUM_OBJECTS)
    prob_map = ProbMap(SIZE)
    # prob_map.generate_prob_random()
    prob_map.generate_prob_from_map(object_map)
    count_map = CountMap(SIZE)
    greedy = WeightedGreedy(prob_map, count_map)
    print(greedy.iterate(object_map, fail_prob))

main()