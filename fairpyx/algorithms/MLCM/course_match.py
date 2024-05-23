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

    :param instance: a fair-course-allocation instance, At first only contains the list of courses
    
    :return instance: a fair-course-allocation instance, with student preferences regarding the courses
    """
    pass

def compute_A_CEEI(student_preferences: List[List[int]], initial_price_vector: List[float], heuristic_params: Dict[str, float]) -> Tuple[List[float], List[List[int]]]:
    """
    Finds a price vector that constitutes an approximate Competitive Equilibrium from Equal Incomes (A-CEEI)
    based on a heuristic algorithm.

    :param student_preferences (list): A list of student preference profiles.
    :param initial_price_vector (list): An initial vector of course prices.
    :param heuristic_params (dict): Parameters for the heuristic algorithm.

    :return tuple:
        - price_vector (list): The price vector that approximates A-CEEI.
        - student_schedules (Instance): The utility-maximizing schedule for each student within their budget.
    """
    # Implementation of the heuristic algorithm to find the A-CEEI price vector
    # This will involve iterating over price vectors, solving MIP for each student, and finding utility-maximizing schedules
    pass


def remove_oversubscription(price_vector: List[float], course_capacities: Dict[str, int], current_allocation: Dict[str, List[int]]) -> Tuple[List[float], Dict[str, List[int]]]:
    """
    Removes oversubscription in courses by iteratively increasing the price of the most oversubscribed course
    until all courses are within capacity limits.

    :param price_vector (list): The current vector of course prices.
    :param course_capacities (dict): A dictionary with course capacities.
    :param current_allocation (dict): The current allocation of students to courses.

    :return tuple:
        - adjusted_price_vector (list): The adjusted price vector after removing oversubscription.
        - updated_allocation (dict): The updated allocation of students to courses with no oversubscription.
    """
    # Implementation of the oversubscription removal process
    # This involves identifying the most oversubscribed courses and adjusting their prices
    pass


def reduce_undersubscription(adjusted_price_vector: List[float], initial_budgets: List[float], current_allocation: Dict[str, List[int]], available_courses: List[str]) -> Tuple[List[float], Dict[str, List[int]], List[float]]:
    """
    Reduces the undersubscription caused by the oversubscription removal process by increasing all students' budgets
    by a fixed percentage and allowing students to select additional courses with available seats.

    :param adjusted_price_vector (list): The price vector after oversubscription removal.
    :param initial_budgets (list): The initial budgets of the students.
    :param current_allocation (dict): The current allocation of students to courses.
    :param available_courses (list): A list of courses with available seats.

    :return tuple:
        - final_price_vector (list): The final price vector after reducing undersubscription.
        - final_allocation (dict): The final allocation of students to courses.
        - updated_budgets (list): The updated budgets of the students.
    """
    # Implementation of the undersubscription reduction process
    # This involves increasing student budgets and allowing them to select additional courses
    pass

def course_allocation_pipeline(student_preferences: List[List[int]], initial_price_vector: List[float], heuristic_params: Dict[str, float], course_capacities: Dict[str, int], current_allocation: Dict[str, List[int]], initial_budgets: List[float], available_courses: List[str]) -> Tuple[List[float], Dict[str, List[int]], List[float]]:
    """
    Orchestrates the course allocation pipeline by calling the three main functions sequentially.

    Parameters:
    :param student_preferences (list): A list of student preference profiles.
    :param initial_price_vector (list): An initial vector of course prices.
    :param heuristic_params (dict): Parameters for the heuristic algorithm.
    :param course_capacities (dict): A dictionary with course capacities.
    :param current_allocation (dict): The current allocation of students to courses.
    :param initial_budgets (list): The initial budgets of the students.
    :param available_courses (list): A list of courses with available seats.

    :return tuple:
        - final_price_vector (list): The final price vector after reducing undersubscription.
        - final_allocation (dict): The final allocation of students to courses.
        - updated_budgets (list): The updated budgets of the students.
    """
    # Step 1: Compute A-CEEI
    price_vector, student_schedules = compute_A_CEEI(student_preferences, initial_price_vector, heuristic_params)
    
    # Step 2: Remove oversubscription
    adjusted_price_vector, updated_allocation = remove_oversubscription(price_vector, course_capacities, current_allocation)
    
    # Step 3: Reduce undersubscription
    final_price_vector, final_allocation, updated_budgets = reduce_undersubscription(adjusted_price_vector, initial_budgets, updated_allocation, available_courses)
    
    return final_price_vector, final_allocation, updated_budgets

