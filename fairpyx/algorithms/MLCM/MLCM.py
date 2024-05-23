"""
Machine Learning-Powered Course Allocation 
Ermis Soumalias, Behnoosh Zamanlooy, Jakob Weissteiner, Sven Seuken
Mon, 3 Oct 2022
https://arxiv.org/abs/2210.00954

Programmer: Ben Dabush and Naama Shiponi
Date: 2024-05
"""


from fairpyx import Instance, AllocationBuilder

def MLCM_algorithm():
    """
    The Machine Learning-Powered Course Allocation algorithm.
    Conection of the CM and  OBIS algorithms.

    :variables instance (Instance) : The instance of the problem.
    :variables prices (list) : The prices of the courses.
    :variables budget (list): The budget of the student.

    :return final_allocation (dict): The final allocation of students to courses.
    
    :pseudo code
        instance = new Instance()
        instance = collect_student_preferences_gui(instance) 
        prices, budget = compute_A_CEEI()
        for each student id:
            student_OBIS = new OBIS(id, instance, prices, budget)
            instance = student_OBIS.main_loop_for_OBIS()
        final_price_vector, final_allocation, updated_budgets = course_allocation_pipeline()
        return final_allocation

        
    """
    pass


if __name__ == "__main__":
    print("This is a library of algorithms for Machine Learning-Powered Course Allocation.")
    print("Please refer to the documentation for more information.")
    print("https://arxiv.org/abs/2210.00954")
    print("Programmer: Ben Dabush and Naama Shiponi")
    final_allocation = MLCM_algorithm()
    print("Final allocation of students to courses:", final_allocation)