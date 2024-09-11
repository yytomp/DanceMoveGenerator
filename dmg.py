# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:23:25 2024

@author: mmtp1023
"""
import random


"""Rhythm"""
base= ['1 2 3 4 ']
sdv1= ['1&2 3 4 ']
sdv2= ['1 2&3 4 ']
sdv3= ['1 2 3&4 ']
simple_triple = ['1&2&3&4 ']
simple_quadruple = ['1&2&3&4&']
off_beat= ['&1&2&3&4']
obv1= ['&1&2 3 4 ']

common_patterns = [base,sdv1,sdv2,sdv3,simple_triple,simple_quadruple,off_beat,obv1]

base2= ['5 6 7 8 ']
sdv12= ['5&6 7 8 ']
sdv22= ['5 6&7 8 ']
sdv32= ['5 6 7&8 ']
simple_triple2 = ['5&6&7&8 ']
simple_quadruple2 = ['5&6&7&8&']
off_beat2= ['&5&6&7&8']
obv12= ['&5&6 7 8 ']

common_patterns2 = [base2,sdv12,sdv22,sdv32,simple_triple2,simple_quadruple2,off_beat2,obv12]


"""Movements""" 

halfBeat = ["Smurf","PepperSeed", "Steve Martin", "The Wop","Camel Walk", "Monastery","Gucci","nae nae", "snake","steps", "cabbage patch", "runningMan"] 
oneBeat = ["Mike Tyson","alf","RunningMan","happy feet", "Robocop","James Brown", "Crab","BK Bounce","Roger Rabbit","Party Machine", "Kick Step", "The Prep"] 

def determine(value):
    if len(value) >= 8:
        head = value[0]
        first = value[1]
        third = value[3]
        fifth = value[5]
        seventh = value[7]
        rules = [head.isnumeric(),
                 first != "&",
                 third != "&",
                 fifth != "&",
                 seventh != "&",
            ]
        if all(rules):
            return oneBeat
        else:
            return halfBeat
        
def calculate(length,prev_pattern_pointer,times):
    """First part of the program makes sure 
    off beat pattern don't mix with & start pattern"""
    pattern_pointer = random.randint(0,length) # int
    if prev_pattern_pointer == 5: 
        pattern_pointer = random.randint(0,length-2)
    prev_pattern_pointer = pattern_pointer
    
    current_move = random.randint(0,len(oneBeat)-1)#return a int
    beat_selection = determine(common_patterns[pattern_pointer][0])
    if(times == 0):
        return (beat_selection[current_move]),(common_patterns[pattern_pointer])
    else:
        return (beat_selection[current_move]),(common_patterns2[pattern_pointer])
    

def dance():
    pattern = [] #maybe don't need this to print out moves
    eight_count = 4 # How many 8 counts there are
    prev_pattern_pointer = 0 
    length = len(common_patterns) - 1 
    
    #logic so off beats work
    for repeat in range(eight_count*2):
        moves = []
        pats = []
        for times in range(2):
            move, pat = calculate(length,prev_pattern_pointer,times)
            moves.append(move)
            pats.append(pat)
        print(moves)
        print(pats)
        
        
dance()


"""
31.May
输出结果希望是动作名称加上所对应的节奏类型 e.g 
Camel Walk
['1&2 3 4']
Camel Walk
['1&2 3 4']
Camel Walk
['1& 2& 3& 4&']
The Prep
['1& 2& 3& 4']
Steve Martin
['1& 2& 3& 4']
Bobby Brown
['&1 &2 &3 &4']
Mike Tyson
['1& 2& 3& 4']
Robocop
['1&2 3 4']

NEXT TODO:
*String value can be indexed 
Seperate current rhythem patterns so we are able to tell if each
value is a halfBeat or a oneBeat 01234567
8 potential values in a bracket [1&2&3&4&]
if 1 != & and 3 != & and 5 != & and 7 != and:
    oneBeat
else:
    halfBeat




"""