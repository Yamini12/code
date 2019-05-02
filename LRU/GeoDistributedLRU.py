# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:46:47 2019

@author: yamin
"""
import datetime
class Lru:
    def __init__(self):
        self.cachesize=3
        self.mem={}
    def add(self,key,value):
        if(len(self.mem)>=self.cachesize):
            last = None
            for i in self.mem:
                 if last==None:
                     last=i
                 elif self.mem[i][1]<self.mem[last][1]:
                     last=i
            del self.mem [last]
              

        self.mem[key]=[value,datetime.datetime.now().isoformat()]



