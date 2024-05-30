from typing import Dict, List, Callable
from fairpyx.instances import Instance

def remove_oversubscription(price_vector: Dict[str, int], student_budgets: List[float],  instance: Instance, epsilon: float, demand_function: Callable):
    """
    Perform oversubscription elimination to adjust course prices.

    :param price_vector: Initial price vector (Dict of str and floats)
    :param budgets: List of student budgets (list of floats)
    :param instance: Instance
    :param demand_function: Function that takes price vector and returns excess demand vector
    :param epsilon: Small value to determine when to stop binary search
    :return: Adjusted price vector (list of floats)
   >>> instance = Instance(
    ...   agent_capacities = {"Alice": 2, "Bob": 3, "Tom": 3}, 
    ...   item_capacities  = {"c1": 1, "c2": 1, "c3": 1}, 
    ...   valuations       = {"Alice": {"c1": 55, "c2": 55, "c3": 100},
    ...                         "Bob": {"c1": 40, "c2": 60, "c3": 40},
    ...                         "Tom": {"c1": 70, "c2": 70, "c3": 100}
    ... })
    >>> initial_prices = [40, 50, 50]
    >>> epsilon = 2
    >>> student_budgets = [90,100,110]
    >>> remove_oversubscription(price_vector, student_budgets, instance, epsilon, demand_function)
    [84, 98, 118]

    """
    pass

def demand_function(p,item_capacities,student_preferences):
    """
    :param p (list): Price vector
    :param item_capacities (dict): Dictionary with course capacities.
    :param student_preferences (dict): Dictionary with student preferences for each course.
    
    :return (list) List of demands for each course.

    >>> student_preferences = {
    ...     "Alice": {"x": 55, "y": 55, "z": 100},
    ...     "Bob": {"x": 40, "y": 60, "z": 40},
    ...     "Tom": {"x": 70, "y": 70, "z": 100}
    ... }
    >>> item_capacities = {"x": 1, "y": 1, "z": 1}
    >>> demand_function([40, 50, 50],item_capacities,student_preferences)
    [2, 2, 2]
    """
    pass
