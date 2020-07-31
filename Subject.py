#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:30:59 2020

@author: akiharma
"""

import numpy as np
import datetime as dt
from SubjectPool import ChadSubjectPool

def isNaN(num):
    return num != num

def dayminute(mtime):
    return 60*mtime.hour + mtime.minute


class SubjectModel():
    general_health_score = None
    gender = None
    age = None
    race = None
    smoker = None
    lifestyleModel = None
    weekworker = None
    profession = None
    
class Subject():    
    def __init__(self):        
        self.model = SubjectModel()
        p = ChadSubjectPool()
        self.model.lifestyleModel = p.sample()
        x = self.model.lifestyleModel.iloc[0] 
        self.model.age = x.age
        self.model.gender = x.male
        self.model.weight = x.weight
        self.model.smoker = x.smokercode
        self.model.race = x.racecode        
        self.model.general_health_score = 1
        self.model.weekworker = True        
        if isNaN(self.model.lifestyleModel.loc["toWork","startTime"]):
            self.model.weekworker = False
        self.mytime = dt.datetime(2020,1,1)         
        
    def step(self, i=1):
        self.mytime += dt.timedelta(minutes = i)
        dmin = dayminute(self.mytime)
    
        if (self.model.weekworker == True) & (self.mytime.weekday() < 5):
            m = self.model.lifestyleModel.copy()
            m = m[m["workday"].apply(lambda x: x in [0,1])]
            out = m[(m["startTime"]<=dmin)&(m["endTime"]>dmin)]

        else:
            m = self.model.lifestyleModel.copy()
            m = m[m["workday"].apply(lambda x: x in [0,2])]    
            out = m[(m["startTime"]<=dmin)&(m["endTime"]>dmin)]
            
        state = out.iloc[out.duration.argmin()]
        health = 1.0-np.std(m["engagement"]) 
                
        return health, state
    
    def intervene(self, action):
        self.model.lifestyleModel.loc[action[0], "engagement"] *= action[1]
        
        
        
        

