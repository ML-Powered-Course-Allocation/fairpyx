"""
Machine Learning-Powered Course Allocation 
Ermis Soumalias, Behnoosh Zamanlooy, Jakob Weissteiner, Sven Seuken
Mon, 3 Oct 2022
https://arxiv.org/abs/2210.00954

Programmer: Ben Dabush and Naama Shiponi
Date: 2024-05
"""
from fairpyx import Instance, AllocationBuilder
from typing import List, Dict, Tuple

def collect_student_preferences_gui(instance: Instance) -> Instance:
    """
    Provides a graphical user interface (GUI) for students to enter their course preferences.

    :param instance (Instance): a fair-course-allocation instance, At first only contains the list of courses
    
    :return instance (Instance): a fair-course-allocation instance, with student preferences regarding the courses
    """
    pass

def compute_A_CEEI(instance: Instance, price_vector: Dict[str, int]) -> Tuple[Dict[str, int], Instance, int]:
    """
    Finds a price vector that constitutes an approximate Competitive Equilibrium from Equal Incomes (A-CEEI)
    based on a heuristic algorithm.

    :param instance (Instance): a fair-course-allocation instance for the student's preference for courses
    :param price_vector (dict): An initial vector of course prices.

    :return tuple:
        - price_vector (dict): The price vector of the courses that approximates A-CEEI.
        - current_allocation (instance): The utility-maximizing schedule for each student within their budget.
        - students_budget (int): Budget for the students
    """
    # Implementation of the heuristic algorithm to find the A-CEEI price vector
    # This will involve iterating over price vectors, solving MIP for each student, and finding utility-maximizing schedules
    pass


def remove_oversubscription(price_vector: Dict[str, int], instance: Instance, current_allocation: Dict[str, List[int]]) -> Tuple[Dict[str, int], Dict[str, List[int]]]:
    """
    Removes oversubscription in courses by iteratively increasing the price of the most oversubscribed course
    until all courses are within capacity limits.

    :param price_vector (dict): The current vector of course prices.
    :param instance (Instance): a fair-course-allocation instance, for course capacities.
    :param current_allocation (dict): The current allocation of students to courses.

    :return tuple:
        - price_vector (dict): The adjusted price vector after removing oversubscription.
        - updated_allocation (dict): The updated allocation of students to courses with no oversubscription.
    """
    # Implementation of the oversubscription removal process
    # This involves identifying the most oversubscribed courses and adjusting their prices
    pass


def reduce_undersubscription(price_vector: Dict[str, int], initial_budgets: List[float], current_allocation: Dict[str, List[int]], instance: Instance) -> Tuple[List[float], Dict[str, List[int]], List[float]]:
    """
    Reduces the undersubscription caused by the oversubscription removal process by increasing all students' budgets
    by a fixed percentage and allowing students to select additional courses with available seats.

    :param price_vector (Dict): The price vector after oversubscription removal.
    :param students_budget (list): The initial budgets of the students.
    :param current_allocation (dict): The current allocation of students to courses.
    :param instance (Instance): a fair-course-allocation instance, for courses with available seats.

    return tuple:
        - final_price_vector (list): The final price vector after reducing undersubscription.
        - final_allocation (dict): The final allocation of students to courses.
        - updated_budgets (list): The updated budgets of the students.
    """
    # Implementation of the undersubscription reduction process
    # This involves increasing student budgets and allowing them to select additional courses
    pass

def course_allocation_pipeline(instance: Instance, price_vector: Dict[str, int], current_allocation: Dict[str, List[int]], students_budget: int) -> Tuple[List[float], Dict[str, List[int]], List[float]]:
    """
    Orchestrates the course allocation pipeline by calling the three main functions sequentially.


    :param instance (Instance): a fair-course-allocation instance, for course capacities and the student's preference for courses
    :param current_allocation (dict): The current allocation of students to courses.
    :param price_vector (dict): An initial vector of course prices.
    :param students_budget (list): The initial budgets of the students.

    return tuple:
        - final_price_vector (list): The final price vector after reducing undersubscription.
        - final_allocation (dict): The final allocation of students to courses.
        - updated_budgets (list): The updated budgets of the students.
    """
    # Step 1: Compute A-CEEI
    price_vector, current_allocation, students_budget = compute_A_CEEI(instance, price_vector)
    
    # Step 2: Remove oversubscription
    adjusted_price_vector, updated_allocation = remove_oversubscription(price_vector, instance, current_allocation)
    
    # Step 3: Reduce undersubscription
    final_price_vector, final_allocation, updated_budgets = reduce_undersubscription(instance, adjusted_price_vector, updated_allocation, students_budget)
    
    return final_price_vector, final_allocation, updated_budgets

