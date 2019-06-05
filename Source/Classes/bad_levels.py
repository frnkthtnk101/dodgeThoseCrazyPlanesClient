'''
bad_levels.py
unused code
'''
from enum import Enum

'''
when a bad level is encountered
we want to know why
'''
class bad_levels(Enum):
    different_version = 1
    different_planes = 2
    complete_type_not_valid = 3
    ticks_go_over = 4
    different_difficulty = 5