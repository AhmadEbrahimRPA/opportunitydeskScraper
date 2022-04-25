#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def fun():
    print("I'm here")

def climbingLeaderboard(ranked, player):
    # Write your code here
    i = 0
    ranked = list(dict.fromkeys(ranked))
    for s in player:
        for r, i in zip(ranked, range(len(ranked))):
            if s >= r:
                print(i + 2)
                break
        else:
            print(i+1)


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))


    #result = climbingLeaderboard(ranked, player)
    climbingLeaderboard(ranked, player)

