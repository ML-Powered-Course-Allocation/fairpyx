"""
Machine Learning-Powered Course Allocation 
Ermis Soumalias, Behnoosh Zamanlooy, Jakob Weissteiner, Sven Seuken
Mon, 3 Oct 2022
https://arxiv.org/abs/2210.00954

Programmer: Ben Dabush and Naama Shiponi
Date: 2024-05
"""

def prepare_data(Di_card, Di_ord):
    """
    Prepare the data for training a machine learning model to predict the utility of different combinations of courses.

    :param Di_card (list): The Di,card data, where each element is a list representing a combination of courses.
    :param Di_ord (list): The Di,ord data, where each element is a list representing a combination of courses.
        
    :return list: The prepared data for training the machine learning model.
    """
    pass

def train_model(x, y):
    """
    Train a machine learning model to predict the utility of different combinations of courses.
    
    Psuedo code:
        θ_0 ← initialize parameters of the ML model M 
        for i=1 to treg  
            lossreg ← 0 
            for each (x,y) in {Xreg,yreg}  
                y' ← (M^(θ_i-1))(x) 
                lossreg ← lossreg + lreg(y, y') + λreg* SUN((θ_i-1)^2) 
            θ_i ← ADAM(θ_i-1, lossreg, ηreg) 
        for i=treg + 1 to (treg + tclass)  
            lossclass ← 0 
            for each ((x1,x2),y) in {Xclass, yclass}
                y1' ← (M^(θ_i-1))(x1) 
                y2' ← (M^(θ_i-1))(x2) 
                y' ← 1\(1+e^(-(y1'- y2'))) 
                lossclass ← lossclass +lclass(y, y') + λclass 
            θi ←ADAM(θi-1, lossclass, ηclass) 
        return θ_(treg+tclass)

    :param x: The input data for training the model.
    :param y: The target values for training the model.

    :return list: Parameters of trained ML model M (new utility)
    """
    pass
