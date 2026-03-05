from backend.algorithms.dijkstra import dijkstra_steps
from backend.algorithms.union_find import union_find_steps

def run_algorithm(name, input_data):

    if name == "dijkstra":
        return dijkstra_steps(input_data)

    if name == "union_find":
        return union_find_steps(input_data)

    return []