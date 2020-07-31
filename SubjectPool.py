#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:40:25 2020

@author: akiharma
"""

import pandas as pd
import numpy as np

def isNaN(num):
    return num != num

class ChadSubjectPool():
    fname = "./data/chad_merged_all_oct17.csv"
    userdata = pd.read_csv(fname)
    uids = userdata[userdata["sportCount"]>0]["CHADID"].unique()
    
    def sample(self):
        uid = np.random.choice(self.uids,1)[0]
        udata = self.userdata[self.userdata["CHADID"] == uid].copy()

        udata.index = udata.segmentType
        udata["workday"] = 0
        udata.loc[["toWork","atWork","toHome","eveningAfterWork"],"workday"]=1
        udata.loc[["freeDayTime","eveningAfterFree"],"workday"]=2
        udata["engagement"] = 0.01
        udata = udata[['startTime', 'endTime', 'duration', 'age', 
                       'weight', 'male', 'racecode', 'smokercode',
                       'workday','engagement']]
        udata.loc["wholeDay","startTime"] = 0
        udata = self.engagement_pattern(udata)
        return udata
                    
    def engagement_pattern(self, udata):
            udata.loc[['awake', 'morning','freeDayTime', 'eveningAfterFree'],
                      "engagement"] = np.random.random(1)[0]*0.5
            udata.loc["atWork","engagement"] = np.random.random(1)[0]*0.1
            udata.loc[['toWork', 'toHome','eveningAfterWork'],
                      "engagement"] = np.random.random(1)[0]*0.8          
            
            return udata
        
        