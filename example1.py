####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Cash'
strategy_name = 'e'
strategy_description = "Betray if oppponent has betrayed more than half the time"

def move(my_history, their_history, my_score, their_score):
  theirB = 0 
  for action in their_history:
    if action == 'b':
      theirB+=1
  if len(their_history)==0:
    return "c"
  else:
    if theirB/len(their_history)>0.5 or their_score > my_score:
      return 'b'
    else:
      return 'c'
  print(theirB)
