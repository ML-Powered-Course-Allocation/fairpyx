import random
import time

from fairpyx.instances import Instance
def A_CEEI(instance:Instance, beta = 100, t = 10, seed=None):
    """
    Perform heuristic search to find the best price vector that matches student preferences and course capacities.

    :param beta (float): Initial budget.
    :param d (function): Function to calculate demands based on price vector.
    :param N (function): Function to generate neighbors of the price vector.
    :param t (float): Time limit for the search.
    :param item_capacities (dict): Dictionary with course capacities.
    :param student_preferences (dict): Dictionary with student preferences for each course.
    :param seed (int): Seed for random number generator.

    :return (tuple) Tuple containing the best price vector and the best error.

    """
    item_capacities = instance.course_capacities
    student_preferences = instance.valuations 

    if seed is not None:
        random.seed(seed)

    best_error = float('inf')
    best_price_vector = None
    start_time = time.time()

    while time.time() - start_time < t:
        p = [random.uniform(0, 1) * beta for _ in range(len(item_capacities))]
        search_error = alpha(d(p,item_capacities,student_preferences),item_capacities)
        tabu_list = []
        steps_without_improvement = 0

        while steps_without_improvement < 5:
            neighbors = N(p,item_capacities,student_preferences)
            found_next_step = False

            while neighbors and not found_next_step:
                p_prime = neighbors.pop(0)
                demands = d(p_prime,item_capacities,student_preferences)

                if demands not in tabu_list:
                    found_next_step = True

            if not neighbors:
                steps_without_improvement = 5
            else:
                p = p_prime
                tabu_list.append(demands)
                current_error = alpha(demands,item_capacities)

                if current_error < search_error:
                    search_error = current_error
                    steps_without_improvement = 0
                else:
                    steps_without_improvement += 1

                if current_error < best_error:
                    best_error = current_error
                    best_price_vector = p

    return best_price_vector, best_error , beta

def alpha(demands,item_capacities):
    """
    Calculate the clearing error based on demands and capacities.
    α = (d(p) - q)^2

    :param demands (list): List of demands for each course.
    :param item_capacities (dict): Dictionary with course capacities.
       
    :returns (float) Clearing error.
    
    :example
    >>> item_capacities = {"x": 1, "y": 2, "z": 2}
    >>> alpha([1, 2, 2], item_capacities)
    0
    >>> alpha([0, 2, 3],item_capacities)
    2
    >>> item_capacities = {"x": 1, "y": 1, "z": 1, "w": 1}
    >>> alpha([1, 1, 1, 1], item_capacities)
    0
    >>> alpha([0, 0, 0, 0], item_capacities)
    4
    """
    return sum(abs(d_i - capacity) for d_i, capacity in zip(demands, item_capacities.values()))

def d(p,item_capacities,student_preferences):
    """
    :param p (list): Price vector
    :param item_capacities (dict): Dictionary with course capacities.
    :param student_preferences (dict): Dictionary with student preferences for each course.
    
    :return (list) List of demands for each course.

    :example
    >>> student_preferences = {
    ...     "Alice": {"x": 55, "y": 55, "z": 100},
    ...     "Bob": {"x": 40, "y": 60, "z": 40},
    ...     "Tom": {"x": 70, "y": 70, "z": 100}
    ... }
    >>> item_capacities = {"x": 1, "y": 2, "z": 2}
    >>> d([1, 1, 1],item_capacities,student_preferences)
    [84, 98, 118]
    """
    demands = {course: 0 for course in item_capacities.keys()}
    for student, preferences in student_preferences.items():
        total_budget = 100
        allocated_budget = sum(p[i] * preferences[course] for i, course in enumerate(item_capacities.keys()))
        if allocated_budget == 0:
            continue
        for course in item_capacities.keys():
            demands[course] += total_budget * preferences[course] / allocated_budget
    return [round(x) for x in list(demands.values())]

def N(p,item_capacities,student_preferences):
    """
    Generate neighbors of the price vector by adding or subtracting small values.

    :param p (list): Price vector

    :return (list) List of neighboring price vectors.
    
    :example
    >>> student_preferences = {
    ...     "Alice": {"x": 55, "y": 55, "z": 100},
    ...     "Bob": {"x": 40, "y": 60, "z": 40},
    ...     "Tom": {"x": 70, "y": 70, "z": 100}
    ... }
    >>> item_capacities = {"x": 1, "y": 2, "z": 2}
    >>> sorted(N([1, 1, 1],item_capacities,student_preferences))
    [[0.9, 1, 1], [1, 0.9, 1], [1, 1, 0.9], [1, 1, 1.1], [1, 1.1, 1], [1.1, 1, 1]]
    """
    neighbors = []
    for i in range(len(p)):
        for delta in [-0.1, 0.1]:
            p_new = p[:]
            p_new[i] = max(0, p_new[i] + delta)
            neighbors.append(p_new)
    neighbors.sort(key=lambda p: alpha(d(p,item_capacities,student_preferences),item_capacities))
    return neighbors


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

#     student_preferences = {
#         "Alice": {"x": 55, "y": 55, "z": 100},
#         "Bob": {"x": 40, "y": 60, "z": 40},
#         "Tom": {"x": 70, "y": 70, "z": 100}
#     }
#     item_capacities = {"x": 1, "y": 2, "z": 2}
#     beta = 100
#     t = 10
#     seed = 42
#     best_price_vector, best_error = A_CEEI(beta, d, N, t, item_capacities, student_preferences,seed)
#     print("Best Price Vector:", best_price_vector)
#     print("Best Error:", best_error)

