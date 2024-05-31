from typing import Dict, List, Callable
from fairpyx.instances import Instance
def reduce_undersubscription(current_allocations: Dict[str, List[int]], price_vector: List[float], instance: Instance, sort_student_list: List[(str, int)] , restricted_demand_function: Callable):
    """
    initial_budgets: List[float], current_allocation: Dict[str, List[int]], instance: Instance
    Perform automated aftermarket allocations with increased budget and restricted allocations.

    :param budgets: List of student budgets (list of floats)
    
    :param current_allocations: Dictionary of current course allocations {student: [courses]}
    :param student_list: List of students ordered by their class year descending and budget surplus ascending
    :param restricted_demand_function: Function to reoptimize student's schedule given a set of courses and budget
    :param instance: (Instance) Dictionary of course capacities
    :return: Updated course allocations

    >>> instance = Instance(
    ...   agent_capacities = {"Alice": 2, "Bob": 3, "Tom": 3}, 
    ...   item_capacities  = {"c1": 1, "c2": 1, "c3": 1, "c4": 1}, 
    ...   valuations       = {"Alice": {"c1": 90, "c2": 60, "c3": 50, "c4": 10},
    ...                         "Bob": {"c1": 57, "c2": 80, "c3": 63, "c4": 20},
    ...                         "Tom": {"c1": 70, "c2": 50, "c3": 95, "c4": 29}
    ... })
    >>> price_vector = [103, 90, 72, 10]
    >>> student_budgets = [110, 100, 90]
    >>> current_allocations = {{"Alice": [1, 0, 0, 0]},
    >>>                          {"Bob": [0, 1, 0, 0]},
    >>>                          {"Tom": [0, 0, 1, 0]}}
    >>> sort_student_list = [("Alice", 7), ("Bob", 10), ("Tom", 18)]
    >>> remove_oversubscription(current_allocations, price_vector, instance, instance, sort_student_list, restricted_demand_function)
    {{"Alice": [1, 0, 0, 1]}, {"Bob": [0, 1, 0, 0]}, {"Tom": [0, 0, 1, 0]}}
    """
    pass

# Example restricted demand function
def restricted_demand_function(student_allocation: List[int], price_vector: List[float], open_course: Dict[str: int]):
    """
    Example function to reoptimize student's schedule given a set of courses and budget.

    :param student: The student to reoptimize
    :param available_courses: List of available courses for the student
    :param budget_multiplier: Multiplier to increase the student's budget
    :return: List of new course allocations
    >>> student_allocation = [1, 0, 0, 0]
    >>> price_vector = [103, 90, 72, 10]
    >>> open_course = {"c4": 1}
    >>> restricted_demand_function(student_allocation, price_vector, open_course)
    [1, 0, 0, 1]
    """
    pass
