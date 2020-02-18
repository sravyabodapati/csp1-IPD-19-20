####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Cash'
strategy_name = 'Randomly generate answers'
strategy_description = '''Generate random answers'''
    
def move(my_history, their_history, my_score, their_score):
    '''Generate random answers.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
import random

def randomanswer():
  int = random.randint(1,2)
  if int == 1:
    return 'c'
  if int == 2:
    return 'b'