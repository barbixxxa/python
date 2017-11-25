'''
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each)
 and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given
  bricks. This is a little harder than it looks and can be done without any loops.


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''

def make_bricks(small, big, goal):
  need_big = goal / 5
  need_small = goal - (need_big*5)
  need_change = need_big - big
  
  if need_big > big:
    small -= (need_change*5)
    big += need_change
  if small >= need_small and big >= need_big:
    return True
  else:
    return False