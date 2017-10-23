#!/bin/python3

import sys
import datetime

def time_delta(t1, t2):
    # Complete this function
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time_second1 = datetime.datetime.strptime(t1,time_format)
    time_second2 = datetime.datetime.strptime(t2,time_format)
    delta = int(abs((time_second1-time_second2).total_seconds()))
    return delta

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
