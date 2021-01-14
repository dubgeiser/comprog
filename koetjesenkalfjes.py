#!/usr/bin/env python3

""" Koetjes en kalfjes

1 koe werpt elk jaar een kalf
In jaar 4 werpt een kalf zelf haar eerste kalf (en wordt dus een koe)

Hoeveel koeien en hoeveel kalveren in jaar 17?
"""

number_of_cows = 1
calves = [0, 0, 0]
end = 17
year = 1

while year <= end:
    number_of_cows += calves[2]
    calves[2] = calves[1]
    calves[1] = calves[0]
    calves[0] = number_of_cows
    print(f"{year}: {number_of_cows} cows, {calves}")
    year += 1

print(f"\nYear {end}: {number_of_cows} cows, {sum(calves)} calves.")


"""
map <Leader>t :wall!\|!./%<cr>

1: 1, [1, 0, 0]
2: 1, [1, 1, 0]
3: 1, [1, 1, 1]
4: 2, [2, 1, 1]
5: 3, [3, 2, 1]
6: 4, [4, 3, 2]
7: 6, [6, 4, 3]
8: 9, [9, 6, 4]
9: ...
"""
