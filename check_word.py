# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 13:41:33 2018

@author: Molly
"""
import re
import numpy as np

def check(word):
    defn = ''
    datafile = open('dictionary/dictionary.txt')
    for line in datafile:
        if not re.match(('^'+word.upper() + '\t'), line) == None:
            defn = strip(line)
            return True, split(defn)
    return False, (split(word+':   This is not an official word in Molly\'s Boggle Extravaganza.'))

def strip(defn):
    out = list(defn)
    for i in range(len(defn)-1,-1,-1):
        if defn[i] == '\t':
            out[i] = ':'
            out.insert(i+1,' ')
            out.insert(i+1,' ')
            out.insert(i+1,' ')
        if defn[i] == '\n' or defn[i] == "\"":
            out.pop(i)
    return(''.join(out))

def split(defn):
    stop_length = 50
    length = len(defn)
    char_list = list(defn)
    lines = []
    for i in range(int(np.ceil(length/stop_length))):
        if(50*(i+1) <= length):
            if(char_list[50*(i+1)] == ' ' or char_list[50*(i+1)] == '-' or char_list[50*(i+1)-1] == ' ' or char_list[50*(i+1)-1] == '-'):
                if(50*(i+1)<=length):
                    lines.append(''.join(char_list[50*i:50*(i+1)]))
            else:
                    lines.append(''.join(char_list[50*i:50*(i+1)]) + '-')
        else:
            lines.append(''.join(char_list[50*i:length]))
    return lines
