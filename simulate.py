#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:32:34 2020

@author: akiharma
"""

import numpy as np
from Subject import Subject

patient = Subject()

for q in range(60*24*14):
    health, state = patient.step()
    if np.random.random(1)[0]>0.99: # Random intervention
        intervention = [state.name, np.random.randn(1)[0]]
        patient.intervene(intervention)
        print("Health after {}".format(str(intervention)))    
        print("{} on {} at {} health: {}".format(state.name,  patient.mytime.date(), 
                                  patient.mytime.time(), health))  
    
    