####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Cash'
strategy_name = 'First ten would be collude, the next five betray, the next ten collude'
strategy_description = '''Follows a pattern. Collude for the first ten. Betray for the next five, then collude again for the next ten.
'''

import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on your own pattern and based on what turn it is on.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    # If the other player has betrayed or this is the last half of the game, 
    for char in their_history:
      if char in their_history or len(their_history)>100: 
        return 'b'               # Betray.
      else:
        return 'c'         # but 90% of the time collude
    
    
    