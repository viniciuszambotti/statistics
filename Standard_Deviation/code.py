'''
Given an array,X, of N integers, calculate and print the standard deviation. Your answer should be in decimal form, 
rounded to a scale of 1 decimal place (i.e.,12.3 format). An error margin of +-0.1  will be tolerated for the standard deviation.
'''

import math

l = [10,40,30,50,20]


mean = sum(l) / len(l)

sum_square_distance = sum([(x - mean) ** 2 for x in l])
result = math.sqrt((sum_square_distance/ len(l)))

print(format(result, '.1f'))

