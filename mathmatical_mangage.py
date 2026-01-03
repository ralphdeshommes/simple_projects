
import math 

intrest_rate = 1
time = 5       #for the time varible it depends on the funciton of it with each equation have diffrent meaing to it
intial_value = 300 # how much money do you have in the begining
coumpounded_times = 6 # this shows how many times in a certain time 
cost_of_investment = 100 # how much money do you need for this investment






# this shows the inrest of 
def simple_intrest():
    simple_intrest = intial_value * intrest_rate * time
    return(simple_intrest)


# this shows the interest of a ce
def compound_intrest():
    compound_intrest = 1 + intrest_rate / coumpounded_times
    compound_intrest = compound_intrest ** (coumpounded_times * time)
    compound_intrest = compound_intrest * intial_value
    return(compound_intrest)
# this shows the intrest of 
def continuosly_compound_intrest():
    continuosly_compound_intrest = math.e ** (intrest_rate * time)
    continuosly_compound_intrest = continuosly_compound_intrest * intial_value
    return(continuosly_compound_intrest)


# This shows the ROI of your investments
def rate_of_investment():
   the_rate =  time / cost_of_investment * 100
   return(the_rate)


    


print(rate_of_investment())


days = 0
















    

   
    