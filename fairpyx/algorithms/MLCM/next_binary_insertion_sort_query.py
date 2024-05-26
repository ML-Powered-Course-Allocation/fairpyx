"""
Machine Learning-Powered Course Allocation 
Ermis Soumalias, Behnoosh Zamanlooy, Jakob Weissteiner, Sven Seuken
Mon, 3 Oct 2022
https://arxiv.org/abs/2210.00954

Programmer: Ben Dabush and Naama Shiponi
Date: 2024-05
"""
from fairpyx.instances import Instance

def NBISQ(id:int, instance:Instance, S:list, x:list, Q:list):
    """
    The Next Binary Insertion Sort Query algorithm.
    Just like (offline) binary insertion sort, in each iteration of the main loop,
    as long as the next comparison point is included in the list Qi of CQs already answered by the student, 
    the search space is reduced in half, based on the student's answer to the CQ, 
    until a CQ is found whose answer is not included in Qi, and that query is returned. 
    Note that this will always happen, as by definition x is a query that cannot be already sorted into 
    the list Si, based on the student's already answered CQs Qi.

    :param id (int): The id of the student.
    :param instance (Instance): The instance of the problem.
    :param S (list): List of sorted schedules based on student’s past responses.
    :param x (list): Newly-generated schedule to be inserted.
    :param Q (list): Student’s comparison queries.

    :return Next CQ to ask the student.

    :pseudo code
        L ← 0 
        R ← n-1 
        while L ≤ R :
            M ← ⌊(L+R)/2⌋ 
            if (x,Si[M])∈Qi :
                if x≻Si[M] :  
                    L←M+1 
                else 
                    R←M-1 
            else 
                return CQ=(x,Si[M]) 

    :example
    >>>  instance = Instance(
    ...  valuations = {"001": {"x": 50, "y": 50, "w": 20, "z": 100}, "002": {"x": 40, "y": 60, "w": 60, "z": 40},"003": {"x": 60, "y": 60, "w": 20, "z": 100}}, 
    ...  agent_capacities = 2, 
    ...  item_capacities = {"x": 1, "y": 1, "w": 1, "z": 2})
    >>> S = [["x", "y"], ["w", "z"], ["x", "z"]]
    >>> x = ["y", "w"]
    >>> Q =  [(("y", "w"), ("x", "y")), (("y", "w"), ("w", "z"))]
    >>> NBISQ("001",instance, S, x, Q)
    (['y', 'w'], ['w', 'z'])
    """
    




