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
    #Current ML model Mi, cardinal data set Di,card, price vector p, permissible schedules Ψi, budget bi, student’s answered comparison queries Qi, list of sorted schedules based on student’s past responses Si, newly-generated schedule to be inserted x
    def __init__(self, model, D_card, prices, schedules, budget , Q, S, x):
        """
        Args:
            model: The current ML model Mi.
            D_card: The cardinal data set Di,card.
            prices: The price vector p.
            schedules: The permissible schedules Ψi.
            budget: The budget bi.
            Q: The student’s answered comparison queries Qi.
            S: The list of sorted schedules based on student’s past responses Si.
            x: The newly-generated schedule to be inserted x.
        """
        self.model = model
        self.D_card = D_card
        self.prices = prices
        self.schedules = schedules
        self.budget = budget
        self.Q = Q
        self.S = S
        self.x = x


    