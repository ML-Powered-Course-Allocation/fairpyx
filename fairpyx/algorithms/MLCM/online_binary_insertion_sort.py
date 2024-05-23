"""
Machine Learning-Powered Course Allocation 
Ermis Soumalias, Behnoosh Zamanlooy, Jakob Weissteiner, Sven Seuken
Mon, 3 Oct 2022
https://arxiv.org/abs/2210.00954

Programmer: Ben Dabush and Naama Shiponi
Date: 2024-05
"""
from fairpyx import Instance, AllocationBuilder

class OBIS:

    def __init__(self, id:int, instance:Instance ,prices:list, budget:list):
        """
        OBIS is designed to generate a sequence of CQs that maximizes the worst case number of schedule
        pairs for which we can infer their relation with respect to the student’s preferences.

        :param id (int): The id of the student.
        :param instance (Instance): The instance of the problem.
        :param prices (list): The prices of the courses.
        :param budget (list): The budget of the student.
        
        :variables schedules (list): permissible schedules,
        :variables D_card (list): The D,card data, where each element is a list representing a combination of courses.
        :variables D_ord (list): All the answers to the comparison questions.
        :variables model (object): The machine learning model.
        :variables S (list): List of sorted schedules based on student’s past responses.
        :variables x (list): Newly-generated schedule to be inserted.
        :variables Q (list): Student’s comparison queries. 

        :methods OBIS_algorithm(self): The Online Binary Insertion Sort algorithm.
        :methods main_loop_for_OBIS(self): The main loop for the OBIS algorithm.
        :methods update_D_card(self): Update the D_card data based on the student’s past responses and model.
        :methods update_D_ord(self): Update the D_ord data based on the student’s past responses and model.
        :methods update_schedules(self): Update the permissible schedules based on the student’s past responses and model.
        """
        self.id = id
        self.instance = instance
        self.prices = prices
        self.budget = budget
        self.schedules = []
        self.D_card = []
        self.model = None
        self.S = []
        self.x = None
        self.D_ord = []
        self.Q = []

        def OBIS_algorithm(self):
            """
            The Online Binary Insertion Sort algorithm.

            :param self
            
            :return list: next CQ to ask the student.
            
            :pseudo code
                if x can be inserted into Si based on the already answered CQs:
                    Si ← Sort(Si,x,Qi) 
                    Di,ord ← All pairwise orderings inferred from Si 
                    Mi ← Train(Di,card,Di,ord) (MVNN model)
                    x ← argmax (x′∈Ψi,x′/ ∈Si:x′·p≤bi Mi(x′)  
                CQ ← NextBinaryInsertionSortQuery(Si,x,Qi) 
                return CQ
            """
            pass

        def main_loop_for_OBIS(self):
            """
            The main loop for the OBIS algorithm.
            
            :param self

            :return list: the student’s utility.

            :pseudo code
                ask the student if he wants to answer a CQ
                while the student wants to answer a CQ:
                    CQ ← OBIS_algorithm()
                    ask the student CQ
                    update_D_card()
                    update_D_ord()
                    update_schedules()
                    ask the student if he wants to answer a CQ
                return the student’s utility

            """
            pass

        def update_D_card(self):
            """
            Update the D_card data based on the student’s past responses and model.

            :param self
            """
            pass

        def update_D_ord(self):
            """
            Update the D_ord data based on the student’s past responses and model.

            :param self
            """
            pass

        def update_schedules(self):
            """
            Update the permissible schedules based on the student’s past responses and model.

            :param self
            """
            pass


    