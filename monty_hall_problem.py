# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:02:37 2018

@author: Sam Purkiss
"""
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np



#Monty Hall problem

def monty_hall(trials = 1000):
    """
    This program tracks the result of the classic Monty Hall problem.
    It compares the actual percentage of success if you switch doors vs. if 
    you stick with the orignal choice. 
    If the Monty Hall solution is correct, then your probability of choosing the winning 
    door should be 2/3 if you switch your choice, and 1/3 if you don't.
    Output is two lists and a chart:
    
        change_probs which shows success rates given door is switched 
        stay_probs which shows success rates given door is not switched 
        charted which plots the results of switching and not switching.    
    """
    #List for win or not results if you switch
    change_result = []
    #List for proportion of current number of wins and losses
    change_probs = []
    #similar lists as above assuming door choice is not switched
    stay_result = []
    stay_probs = []
    
    counter = 0
    
    while counter < trials:
        #reset the doors so all are blank and then assign one at random to take a value of 1
        #1 indicates a win, 0 indicates a loss
        doors = [0,0,0]
        rand_no = random.randint(0,2)
        doors[rand_no] = 1
        
        #Pick a door at random - at this stage you have 1/3 probability of being right so random is fine
        selected_door = random.randint(0,2)
        
        #Monty hall reveals a door that's not a winner
        #The code does this by cycling through the two remaning doors and picking one that's not a winner
        if doors[selected_door-1] != 1:
            opened_door = selected_door-1
        elif doors[selected_door-2] !=1:
            opened_door = selected_door-2
            
        #Now remove the two doors to leave only one result
        #Track what the result is if you stayed
        initial_door_result  = doors.pop(selected_door)        
        doors.pop(opened_door)
        #There's only one door left
        new_door_result = doors[0]
                
        #add results of changing door selection
        change_result.append(new_door_result)
        #calculate the percentage of times the correct door was selected
        current_percent = sum(change_result)/len(change_result)
        change_probs.append(current_percent)
       
        #add results of not changing door selection
        stay_result.append(initial_door_result)
        stay_percent = sum(stay_result)/len(stay_result)          
        stay_probs.append(stay_percent)
        
        
        counter+=1
    
    #create graph showing results
    charted = plot_data(change_probs, stay_probs)
    
    return(change_probs, 
           stay_probs, 
           charted)
    
    

def plot_data(change_probs, stay_probs):
    """
    Charts the success rate of changing and not changing
    the door choice.
    Outputs the chart
    """
    axis_points = np.linspace(0,1, num = 11)
    
    fig, ax = plt.subplots()
    ax.plot(change_probs, 'b-', stay_probs, 'r-')
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    plt.xlabel('Number of Trials')
    plt.ylabel('Total successes')
    plt.title('Monty Hall Problem')
    plt.legend(('Change Doors', 'Don\'t Change Doors'))
    plt.yticks(axis_points)
    
    return fig
    
        
